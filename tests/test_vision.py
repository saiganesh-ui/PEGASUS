from modules.vision.vision import Vision

vision = Vision()

result = vision.analyze("test.png")

print(result.width)
print(result.height)
print(result.mode)
print(result.format)