"""
Memory Judge
Project PEGASUS
"""


class MemoryJudge:

    IMPORTANT_KEYS = {

        "name",
        "age",
        "city",
        "college",
        "github",
        "laptop",
        "phone",
        "email",
        "address",
        "occupation",
        "birthday",
        "website",
        "language",
        "dream",
        "favorite_game",
        "tool",
        "favorite_language",
        "favorite_ide",
        "favorite_editor",
        "favorite_os",
        "favorite_browser",
        "favorite_music",
        "favorite_movie",

    }

    def should_store(self, key, value):

        key = key.lower()

        if key in self.IMPORTANT_KEYS:
            return True

        if len(value) > 2:
            return True

        return False