import pytesseract
from PIL import Image
def parse_string_from_image(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'D://Tesseract-OCR//tesseract.exe'
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

p = parse_string_from_image("captcha.png")
print(p)