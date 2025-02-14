# Burmese OCR Tool

A Python-based GUI application for extracting Burmese and English text from PDF documents using Optical Character Recognition (OCR). This tool is specifically optimized for documents containing mixed Burmese and English text, making it ideal for processing Myanmar language documents that include English terms.

## Features

- User-friendly graphical interface
- Supports mixed Burmese and English text recognition
- Real-time progress tracking and preview
- Exports results in Markdown format
- Maintains original document formatting
- Cross-platform compatibility (Windows, Linux, macOS)

## Prerequisites

Before running the application, you need to install:

1. Python 3.6 or higher
2. Tesseract OCR with Burmese language support
3. Required Python packages
4. Tkinter (Python's GUI package)

### Installing Python and Tkinter

#### Windows
1. Download and install Python from [python.org](https://python.org)
   - Make sure to check "Add Python to PATH" during installation
   - Tkinter comes pre-installed with Python on Windows

#### macOS
1. Install Python and Tkinter using Homebrew:
```bash
brew install python@3.11  # or your preferred version
brew install python-tk@3.11
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3
sudo apt install python3-tk
```

### Installing Tesseract OCR

#### Windows
1. Download and install Tesseract from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
2. Add Tesseract to your system PATH
3. Download Burmese language data file (`mya.traineddata`) and place it in the Tesseract tessdata directory

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-mya
```

#### macOS
```bash
brew install tesseract
brew install tesseract-lang  # This includes Burmese language support
```

### Installing Python Dependencies

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yethihahtwe/Burmese-OCR.git
cd Burmese-OCR
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python script.py
```

2. Using the GUI:
   - Click "Browse" to select your input PDF file
   - Choose an output location for the markdown file
   - Click "Start OCR" to begin the process
   - Monitor progress in the progress bar
   - Preview the extracted text in real-time
   - The final result will be saved as a markdown file

## Output Format

The tool generates a markdown (.md) file containing:
- Document metadata (filename, generation time)
- Page-by-page text extraction
- Preserved formatting for both Burmese and English text
- Clear separation between pages

Example output:
```markdown
# OCR Results - document.pdf

Generated on: 2025-02-14 21:38:35

Total pages: 1

---

## Page 1

```burmese
[Extracted text here]
```

---
```

## Troubleshooting

1. Tesseract not found error:
   - Ensure Tesseract is installed correctly
   - Verify the PATH environment variable includes Tesseract
   - Check if the Burmese language pack is installed

2. Poor recognition quality:
   - Ensure the PDF is of good quality
   - Check if the text is properly formatted in the original document
   - Verify that the Burmese font is standard and not a custom font

3. Tkinter not found error:
   - Windows: Reinstall Python and make sure to select Tcl/Tk during installation
   - macOS: Install python-tk using `brew install python-tk@3.11`
   - Linux: Install using `sudo apt install python3-tk`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Tesseract OCR for providing the OCR engine
- PyMuPDF for PDF processing capabilities
- The Myanmar NLP community for language support

## Contact

For any queries or suggestions, please open an issue in the GitHub repository.
