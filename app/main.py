# from app.ocr.nougat_loader import extract_text_from_image

# print(extract_text_from_image("test_inputs/sample.jpeg"))
# the above code was for extracting teh text from handwritten jpg file

from app.ocr.ocr_pipeline import run_ocr

result = run_ocr("test_inputs/sample.jpeg")

print(result)
