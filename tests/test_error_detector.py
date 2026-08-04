from modules.vision.error_detector import ErrorDetector

detector = ErrorDetector()

text = """

Traceback (most recent call last):

ModuleNotFoundError:
No module named 'vision'

"""

result = detector.detect(text)

print(result)