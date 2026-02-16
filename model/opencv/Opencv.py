import cv2
import numpy as np
import pytesseract

def getTextFromImage(image):
    # Convert to OpenCV format
    np_img = np.array(image)
    if np_img.shape[2] == 4:  # RGBA
        np_img = cv2.cvtColor(np_img, cv2.COLOR_RGBA2BGR)
    else:
        np_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    
    # Preprocessing
    gray = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)

    # Optional: Apply thresholding to improve OCR
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Perform OCR default: --psm 7
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789>-'  # PSM 7 = treat the image as a single line of text
    text = pytesseract.image_to_string(resized, config=custom_config)

    print("Extracted Text:", text.strip())
    return text

def getTextFromImage2(image):
    # Convert to OpenCV format
    np_img = np.array(image)
    if np_img.shape[2] == 4:  # RGBA
        np_img = cv2.cvtColor(np_img, cv2.COLOR_RGBA2BGR)
    else:
        np_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    
    gray = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)

    # Upscale FIRST
    gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    # Light blur to reduce anti-alias noise
    gray = cv2.GaussianBlur(gray, (3,3), 0)

    # Simple binary threshold (NOT OTSU)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    resized = cv2.resize(thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Perform OCR default: --psm 7
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789>-'  # PSM 7 = treat the image as a single line of text
    text = pytesseract.image_to_string(resized, config=custom_config)

    print("Extracted Text:", text.strip())
    return text
