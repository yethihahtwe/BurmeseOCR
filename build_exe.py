import PyInstaller.__main__
import os

def build_executable():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    PyInstaller.__main__.run([
        'main.py',  # Your main Python script
        '--name=BurmeseOCR',
        '--windowed',  # For GUI applications
        '--onefile',  # Create a single executable file
        '--icon=assets/icon.ico',  # Path to your icon file
        '--add-data=assets;assets',  # Include asset files
        '--noconsole',  # Don't show console window
        f'--workpath={os.path.join(current_dir, "build")}',
        f'--distpath={os.path.join(current_dir, "dist")}',
        '--clean'  # Clean PyInstaller cache
    ])

if __name__ == '__main__':
    build_executable()