# Install tesseract on your machine. (Windows 10)
# Then execute to code below for OCR.
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
#pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # for windows its requred but for other os it not requred
#pytesseract.pytesseract.tesseract_cmd="/etc/apt/sources.list"
print(pytesseract.image_to_string(Image.open('rt.jpg'), lang='eng'))# to extract in hindi.
# print(pytesseract.image_to_string(Image.open('rt.jpg'), lang='hin'))# to extract in english.
