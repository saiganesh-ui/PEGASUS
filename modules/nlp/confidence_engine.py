"""
Confidence Engine
Project PEGASUS
"""

class ConfidenceEngine:

    def score(self, intent, entity):

        # -----------------------------------------
        # UNKNOWN INTENT
        # -----------------------------------------

        if intent in (None, "unknown"):

            return 0.0

        # -----------------------------------------
        # INTENTS THAT DON'T REQUIRE AN ENTITY
        # -----------------------------------------

        no_entity_required = {
            "greeting",
            "how_are_you",
            "running_apps",
            "active_window",
            "what_am_i_doing",
            "knowledge",
            "system",
            "status",
            "history",
            "time",
            "date",
            "day",
            "help",
            "vision"
        }

        if intent in no_entity_required:

            return 1.0

        # -----------------------------------------
        # ENTITY REQUIRED
        # -----------------------------------------

        if entity is None:

            return 0.0

        if not isinstance(entity, dict):

            return 0.0

        # -----------------------------------------
        # CHECK ENTITY VALUES
        # -----------------------------------------

        for key, value in entity.items():

            if value is None:

                return 0.0

            if isinstance(value, str):

                if not value.strip():

                    return 0.0

        # -----------------------------------------
        # SPECIFIC COMMAND VALIDATION
        # -----------------------------------------

        if intent in {
            "open",
            "close",
            "restart",
            "focus"
        }:

            app = entity.get("app")

            if not app or not app.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # SEARCH
        # -----------------------------------------

        if intent == "search":

            query = entity.get("query")

            if not query or not query.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # OPEN FOLDER
        # -----------------------------------------

        if intent == "open_folder":

            folder = entity.get("folder")

            if not folder or not folder.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # MEMORY
        # -----------------------------------------

        if intent == "remember":

            key = entity.get("key")
            value = entity.get("value")

            if not key or not value:

                return 0.0

            return 1.0

        if intent in {"recall", "forget"}:

            key = entity.get("key")

            if not key or not key.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # FILE OPERATIONS
        # -----------------------------------------

        if intent in {
            "create_folder",
            "create_file",
            "delete_folder",
            "delete_file",
            "rename_folder"
        }:

            name = entity.get("name")

            if not name or not name.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # WEATHER
        # -----------------------------------------

        if intent == "weather":

            city = entity.get("city")

            if not city or not city.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # REMINDER
        # -----------------------------------------

        if intent == "reminder":

            task = entity.get("task")

            if not task or not task.strip():

                return 0.0

            return 1.0

        # -----------------------------------------
        # DEFAULT
        # -----------------------------------------

        return 0.8