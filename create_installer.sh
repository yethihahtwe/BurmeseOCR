#!/bin/bash

# Install innosetup via wine
wget https://files.jrsoftware.org/is/6/innosetup-6.2.2.exe
wine innosetup-6.2.2.exe /VERYSILENT /SUPPRESSMSGBOXES

# Compile the installer
wine 'C:\Program Files (x86)\Inno Setup 6\ISCC.exe' installer_script.iss

# The installer will be in the installer directory