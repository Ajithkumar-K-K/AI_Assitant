import pytesseract
import os
from PIL import Image
import sys
import tempfile

# Set the path to tesseract.exe
if getattr(sys, 'frozen', False):
    # If running as a PyInstaller executable
    base_dir = sys._MEIPASS  # Temporary folder where PyInstaller extracts files
else:
    # If running as a Python script
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Update the path to tesseract executable within the base directory
tesseract_path = os.path.join(base_dir, 'Tesseract-OCR', 'tesseract.exe')

# Set the path for pytesseract to locate tesseract.exe
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def extract_text_from_file(file_path):
    """Extract text from the image file at the given path."""
    
    # Open the image file
    try:
        image = Image.open(file_path)
    except Exception as e:
        print(f"Error opening image file: {e}")
        return ""

    # Extract text using pytesseract
    text = pytesseract.image_to_string(image)

    # Delete the image file after extracting the text
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error deleting image file: {e}")

    return text

# Example usage
if __name__ == "__main__":
    # Create a temporary image file if needed (or use an existing one)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_image_file:
        image_path = tmp_image_file.name

    # You can save an image or test with a dummy image path
    # Assuming you already have an image saved at image_path, pass it to the function
    extracted_text = extract_text_from_file(image_path)

    print("Extracted Text:", extracted_text)
