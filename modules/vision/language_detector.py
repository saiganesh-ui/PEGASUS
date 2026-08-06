"""
Language Detector
Project PEGASUS
Author: Sai Ganesh
"""


class LanguageDetector:

    LANGUAGES = {

        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".html": "HTML",
        ".css": "CSS",
        ".php": "PHP",
        ".sql": "SQL",
        ".json": "JSON",
        ".xml": "XML",
        ".md": "Markdown",
        ".txt": "Text"

    }

    def detect(self, filename):

        if not filename:

            return None

        if isinstance(filename, dict):

            filename = filename.get("name")

        if not filename:

            return None

        filename = filename.lower()

        for extension, language in self.LANGUAGES.items():

            if filename.endswith(extension):

                return {

                    "name": language,
                    "confidence": 1.0

                }

        return None