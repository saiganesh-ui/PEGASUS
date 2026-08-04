from modules.vision.vision import Vision

vision = Vision()

result = vision.analyze_screen()

print("Width :", result.width)
print("Height:", result.height)
print("Format:", result.format)
print("Mode  :", result.mode)