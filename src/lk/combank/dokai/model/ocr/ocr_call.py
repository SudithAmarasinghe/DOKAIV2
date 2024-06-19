# # from ocr_module import TesseractOCR
# from model.ocr.ocr_module import TesseractOCR

# def perform_ocr(image_path):
#     """
#     Function to perform OCR using TesseractOCR class.

#     Args:
#         image_path (str): The path to the image file.

#     Returns:
#         str: The extracted text from the image.
#     """
#     ocr = TesseractOCR()
#     text = ocr.ocr_image(image_path)
#     return text


from model.ocr.ocr_module import TesseractOCR

def perform_ocr(image_path, tesseract_cmd=None):
    """
    Function to perform OCR using TesseractOCR class.

    Args:
        image_path (str): The path to the image file.
        tesseract_cmd (str, optional): The path to the tesseract executable.

    Returns:
        str: The extracted text from the image.
    """
    ocr = TesseractOCR(tesseract_cmd=tesseract_cmd)
    text = ocr.ocr_image(image_path)
    return text
