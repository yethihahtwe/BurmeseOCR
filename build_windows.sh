#!/bin/bash

# Install Windows Python via Wine
wget https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
wine python-3.9.0-amd64.exe /quiet InstallAllUsers=1 PrependPath=1

# Install requirements in Wine Python
wine python -m pip install -r requirements.txt

# Build the executable
wine python -m PyInstaller \
    --name=BurmeseOCR \
    --windowed \
    --onefile \
    --icon=assets/icon.ico \
    --add-data='assets;assets' \
    --noconsole \
    main.py

# The Windows executable will be in dist/BurmeseOCR.exe