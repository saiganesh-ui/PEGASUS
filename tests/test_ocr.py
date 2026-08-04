from modules.vision.ocr import OCR

ocr = OCR()

text = ocr.read("capture.png")

print("Detected Text:")
print("-" * 40)
print(text)