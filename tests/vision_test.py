from modules.vision.screen_analyzer import ScreenAnalyzer

text = """
Visual Studio Code

entity_extractor.py

Line 52

ModuleNotFoundError
"""

analyzer = ScreenAnalyzer()

result = analyzer.analyze(text)

print(result.to_dict())