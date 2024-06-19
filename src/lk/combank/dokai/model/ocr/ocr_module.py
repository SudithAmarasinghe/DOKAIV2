# import pytesseract
# import cv2

# class TesseractOCR:
#     def __init__(self):
#         # Any initialization if needed
#         pass

#     def ocr_image(self, image_path):
#         """
#         Perform OCR on the given image and return the extracted text.

#         Args:
#             image_path (str): The path to the image file.

#         Returns:
#             str: The extracted text from the image.
#         """
#         image = cv2.imread(image_path)
#         if image is None:
#             raise FileNotFoundError(f"Image not found: {image_path}")
#         text = pytesseract.image_to_string(image)
#         cleaned_text = text.replace('\n', ' ')  # Remove newlines
#         return text



import pytesseract
import cv2

class TesseractOCR:
    def __init__(self, tesseract_cmd=None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    
    def ocr_image(self, image_path):
        """
        Perform OCR on the given image and return the extracted text.

        Args:
            image_path (str): The path to the image file.

        Returns:
            str: The extracted text from the image.
        """
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found: {image_path}")
        text = pytesseract.image_to_string(image)
        cleaned_text = text.replace('\n', ' ')  # Remove newlines
        return cleaned_text
