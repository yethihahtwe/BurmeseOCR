import fitz  # PyMuPDF
import os
from PIL import Image
import pytesseract
import io
from datetime import datetime
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from threading import Thread

class BurmeseOCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Burmese OCR Tool")
        self.root.geometry("800x600")
        
        # Configure grid weight
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        
        # Variables
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.status = tk.StringVar(value="Ready")
        self.progress = tk.DoubleVar(value=0.0)
        
        # Create GUI elements
        self.create_input_frame()
        self.create_progress_frame()
        self.create_output_frame()
        
        # Set Tesseract OCR config
        os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/5/tessdata'
        self.custom_config = r'--oem 3 --psm 6 -l mya+eng'
        
    def create_input_frame(self):
        input_frame = ttk.LabelFrame(self.root, text="Input", padding="5")
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        ttk.Label(input_frame, text="PDF File:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.input_file, width=50).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_input).grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(input_frame, text="Output File:").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.output_file, width=50).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(input_frame, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=5, pady=5)
        
        ttk.Button(input_frame, text="Start OCR", command=self.start_ocr).grid(row=2, column=0, columnspan=3, pady=10)
        
    def create_progress_frame(self):
        progress_frame = ttk.LabelFrame(self.root, text="Progress", padding="5")
        progress_frame.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress, maximum=100)
        self.progress_bar.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        
        ttk.Label(progress_frame, textvariable=self.status).grid(row=1, column=0, padx=5, pady=5)
        
        progress_frame.grid_columnconfigure(0, weight=1)
        
    def create_output_frame(self):
        output_frame = ttk.LabelFrame(self.root, text="Preview", padding="5")
        output_frame.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        
        self.preview_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=80, height=20)
        self.preview_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_rowconfigure(0, weight=1)
        
    def browse_input(self):
        filename = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.input_file.set(filename)
            # Auto-set output filename
            output_filename = os.path.splitext(filename)[0] + "_extracted.md"
            self.output_file.set(output_filename)
            
    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            title="Save markdown file",
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")]
        )
        if filename:
            self.output_file.set(filename)
            
    def update_progress(self, current, total):
        progress = (current / total) * 100
        self.progress.set(progress)
        self.root.update_idletasks()
        
    def update_status(self, message):
        self.status.set(message)
        self.root.update_idletasks()
        
    def update_preview(self, text):
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(tk.END, text)
        
    def convert_pdf_to_images_and_ocr(self, pdf_path, output_md):
        try:
            doc = fitz.open(pdf_path)
            text_data = []
            
            md_content = f"# OCR Results - {os.path.basename(pdf_path)}\n\n"
            md_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            md_content += f"Total pages: {len(doc)}\n\n---\n\n"
            
            for page_num in range(len(doc)):
                self.update_status(f"Processing page {page_num + 1}/{len(doc)}")
                self.update_progress(page_num + 1, len(doc))
                
                page = doc[page_num]
                zoom = 3
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat)
                
                img_data = pix.tobytes("png")
                img = Image.open(io.BytesIO(img_data))
                img = img.convert('L')
                
                try:
                    text = pytesseract.image_to_string(img, config=self.custom_config)
                    text = text.replace('|', 'I').replace('၀', '0').replace('သ်', 'ာ')
                    text = text.replace('\n\n', '\n').strip()
                    
                    text_data.append({
                        'Page': page_num + 1,
                        'Text': text
                    })
                    
                    md_content += f"## Page {page_num + 1}\n\n"
                    md_content += f"```burmese\n{text}\n```\n\n"
                    md_content += "---\n\n"
                    
                    # Update preview periodically
                    if (page_num + 1) % 1 == 0:  # Update every page
                        self.update_preview(md_content)
                        
                except Exception as e:
                    error_message = f"OCR error on page {page_num + 1}: {str(e)}"
                    print(error_message)
                    md_content += f"## Page {page_num + 1}\n\n"
                    md_content += f"Error: {error_message}\n\n"
                    md_content += "---\n\n"
            
            with open(output_md, 'w', encoding='utf-8') as f:
                f.write(md_content)
                
            self.update_status("OCR completed successfully!")
            self.update_preview(md_content)
            messagebox.showinfo("Success", "OCR process completed successfully!")
            
            doc.close()
            return text_data
            
        except Exception as e:
            error_msg = f"Error processing PDF: {str(e)}"
            self.update_status(error_msg)
            messagebox.showerror("Error", error_msg)
            return None
            
    def start_ocr(self):
        if not self.input_file.get() or not self.output_file.get():
            messagebox.showerror("Error", "Please select both input and output files!")
            return
            
        # Reset progress
        self.progress.set(0)
        self.status.set("Starting OCR process...")
        self.preview_text.delete(1.0, tk.END)
        
        # Start processing in a separate thread
        Thread(target=self.convert_pdf_to_images_and_ocr, 
               args=(self.input_file.get(), self.output_file.get()),
               daemon=True).start()

def main():
    root = tk.Tk()
    app = BurmeseOCRApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()