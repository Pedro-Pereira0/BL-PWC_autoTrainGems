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

    # Perform OCR
    custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789>-'  # PSM 7 = treat the image as a single line of text
    text = pytesseract.image_to_string(resized, config=custom_config)

    print("Extracted Text:", text.strip())
    return text