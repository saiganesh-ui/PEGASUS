"""
Error Detector
Project PEGASUS
"""

ERRORS = {

    "ModuleNotFoundError":
        "Python couldn't find the requested module.",

    "ImportError":
        "Python failed to import a module.",

    "AttributeError":
        "The object doesn't contain the requested attribute.",

    "TypeError":
        "A function or operation received the wrong data type.",

    "NameError":
        "A variable or function name doesn't exist.",

    "SyntaxError":
        "Python detected invalid syntax.",

    "IndentationError":
        "The indentation in the code is incorrect.",

    "FileNotFoundError":
        "The requested file could not be found.",

    "KeyError":
        "The requested dictionary key doesn't exist.",

    "ValueError":
        "A function received an invalid value.",

    "IndexError":
        "The requested list index is out of range.",

    "PermissionError":
        "Permission was denied while accessing a file.",

    "RuntimeError":
        "Python encountered a runtime problem."
}


class ErrorDetector:

    def detect(self, text):

        for error, explanation in ERRORS.items():

            if error.lower() in text.lower():

                return {

                    "error": error,

                    "explanation": explanation

                }

        return None