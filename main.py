import os
from PIL import Image
import pytesseract
from googletrans import Translator

input_folder = "input"
output_folder = "output"

for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        # Open the image file
        image = Image.open(os.path.join(input_folder, filename))
        # Extract text from the image using OCR
        text = pytesseract.image_to_string(image, lang='eng')
        # Translate the text to the desired language
        translator = Translator()
        translated_text = translator.translate(text, dest='fr').text
        # Create a new image with the translated text
        new_image = Image.new('RGB', image.size, (255, 255, 255))
        new_image_draw = ImageDraw.Draw(new_image)
        new_image_draw.text((0, 0), translated_text)
        # Save the new image in the output folder
        new_image.save(os.path.join(output_folder, filename))