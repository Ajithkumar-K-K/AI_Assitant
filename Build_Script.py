import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to your main script
main_script = os.path.join(current_dir, 'key_listener.py')

# Define the path to Tesseract-OCR
tesseract_path = os.path.join(current_dir, 'Tesseract-OCR')

# Define any additional data files or folders
additional_files = [
    ('Tesseract-OCR', 'Tesseract-OCR'),
    ('main.py', '.'),  
    ('extract_text.py', '.'), 
    ('recommendations.py', '.'), 
    ('notification.py', '.'), 
    ('ScreenClipTool.py', '.')
]

# Build the command for PyInstaller
command = [
    main_script,
    '--onefile',
    '--noconsole',
    f'--add-data={tesseract_path};Tesseract-OCR',
    '--name=WindowsAssist',
    # '--icon=app_icon.ico',  # Uncomment this line if you have an app icon
    '--hidden-import=PIL._tkinter_finder',
    '--hidden-import=pytesseract',
    '--hidden-import=keyboard',
    '--hidden-import=extract_text',
    '--hidden-import=recommendations',
    '--hidden-import=ScreenClipTool',
    '--hidden-import=notification',
]

# Add additional files
for src, dst in additional_files:
    full_src = os.path.join(current_dir, src)
    command.append(f'--add-data={full_src};{dst}')

# Run PyInstaller
PyInstaller.__main__.run(command)