from PIL import Image
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'
im = Image.open("input/1.jpg") 
text = pytesseract.image_to_string(im, lang = 'kor') 

print(text)