import fitz  # PyMuPDF
from PIL import Image
import pytesseract

# Set the path to the Tesseract OCR executable (change this path based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image_pdf(pdf_path):
    # Open the PDF file using PyMuPDF
    pdf_document = fitz.open(pdf_path)

    # Initialize text variable to store extracted text
    text = ""

    # Iterate through each page
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Get the image data for the page
        pixmap = page.get_pixmap()

        # Convert the image data to a Pillow image
        image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)

        # Use OCR to extract text from the image
        extracted_text = pytesseract.image_to_string(image)

        # Append the extracted text to the result
        text += extracted_text

    # Close the PDF document
    pdf_document.close()

    return text
def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)
# Replace 'your_image_based_pdf.pdf' with the path to your image-based PDF file
pdf_path = 'Cam IELTS 15 bản siêu đẹp by thesol.edu.vn.pdf'
extracted_text = extract_text_from_image_pdf(pdf_path)
# Print or use the extracted text as needed
print(extracted_text)
save_text_to_file(extracted_text, "Udacity.txt")