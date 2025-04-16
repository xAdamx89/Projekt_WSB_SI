import pytesseract
import cv2
import numpy as np


def odczyt_OCR(pil_image):
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray, lang='pol')

    return text