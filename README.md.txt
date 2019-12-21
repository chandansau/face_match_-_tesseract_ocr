----
Face_recognition
1. sudo apt-get install python3-venv
2. python3 -m venv ./venv
3. sourcr venv/bin/active
4. sudo apt-get update
5. sudo apt-get install build-essential cmake
6. pip install dlib
7. pip install face_recognition
8. code: 
# The FaceMatching algorithm is also working now. 
# Please find the code below.

import face_recognition
known_image = face_recognition.load_image_file("E1.jpg")
unknown_image = face_recognition.load_image_file("E6.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)

-----------------------------------------------------

Tesseract-ocr
1. sudo apt install tesseract-ocr
2. sudo apt install libtesseract-dev
3. Note for Ubuntu users: In case apt is unable to find the package try adding universe entry to the sources.list file as shown below.

sudo vi /etc/apt/sources.list

Copy the first line "deb http://archive.ubuntu.com/ubuntu bionic main" and paste it as shown below on the next line.
If you are using a different release of ubuntu, then replace bionic with the respective release name.

deb http://archive.ubuntu.com/ubuntu bionic universe
4. pip install pytesseract

5. code:

# Install tesseract on your machine. (Windows 10)
# Then execute to code below for OCR.
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
# for windows its requred but for other os it not requred
#pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

print(pytesseract.image_to_string(Image.open('rt.jpg'), lang='eng'))# to extract in hindi.
# print(pytesseract.image_to_string(Image.open('rt.jpg'), lang='hin'))# to extract in english.

