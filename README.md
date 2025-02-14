# Burmese OCR

A cross-platform OCR application for Burmese text recognition.

## Building the Windows Installer

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Install Tesseract OCR:
   - Download and install from: https://github.com/UB-Mannheim/tesseract/wiki
   - Add Tesseract to your system PATH

3. Install Inno Setup:
   - Download and install from: https://jrsoftware.org/isdl.php

4. Build the executable:
   ```
   python build_exe.py
   ```

5. Create the installer:
   - Open Inno Setup Compiler
   - Open `installer_script.iss`
   - Click Build > Compile

The installer will be created in the `installer` directory.

## Development

- All development should be done in the `dev` branch
- Create pull requests to merge changes into `main`
