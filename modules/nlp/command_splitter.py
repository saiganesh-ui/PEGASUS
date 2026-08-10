"""
Command Splitter
Project PEGASUS
"""

import re


class CommandSplitter:

    COMMAND_STARTERS = [

        "open ",
        "launch ",
        "run ",
        "start ",
        "execute ",

        "close ",
        "kill ",
        "terminate ",

        "search ",
        "google ",
        "find ",
        "look up ",

        "create folder ",
        "create file ",

        "delete folder ",
        "delete file ",

        "rename folder ",

        "focus ",
        "switch to ",
        "activate ",

        "restart ",
        "reopen ",
        "reload ",

        "remember ",
        "forget ",

        "remind me ",
        "weather",

        "what ",
        "who ",
        "where ",

        "show ",
        "list ",

        "analyze screen",
        "look at screen",
        "read screen",
        "scan screen"
    ]

    def split(self, command):

        command = command.strip()

        if not command:
            return []

        # Normalize repeated spaces
        command = re.sub(
            r"\s+",
            " ",
            command
        )

        # Remove trailing punctuation
        command = command.rstrip(" .!?")

        final_commands = []

        # -------------------------------------------------
        # SEMICOLON
        # Semicolon is always treated as a separator.
        # -------------------------------------------------

        semicolon_parts = re.split(
            r"\s*;\s*",
            command
        )

        for part in semicolon_parts:

            part = part.strip()

            if not part:
                continue

            # -------------------------------------------------
            # SMART COMMA SPLITTING
            # Only split comma when the text AFTER the comma
            # starts another known command.
            # -------------------------------------------------

            comma_parts = self._split_comma(part)

            for comma_part in comma_parts:

                comma_part = comma_part.strip()

                if not comma_part:
                    continue

                # -------------------------------------------------
                # SMART "AND" SPLITTING
                # -------------------------------------------------

                subparts = self._split_and(
                    comma_part
                )

                final_commands.extend(
                    subparts
                )

        return final_commands

    # =================================================
    # SMART COMMA SPLITTER
    # =================================================

    def _split_comma(self, text):

        matches = list(
            re.finditer(
                r"\s*,\s*",
                text
            )
        )

        if not matches:

            return [text.strip()]

        commands = []

        start = 0

        for match in matches:

            left = text[
                start:match.start()
            ].strip()

            right = text[
                match.end():
            ].strip()

            # Only split if the text after the comma
            # actually looks like a new command.

            if self._starts_command(right):

                if left:

                    commands.append(left)

                start = match.end()

        remaining = text[start:].strip()

        if remaining:

            commands.append(remaining)

        return commands

    # =================================================
    # SMART "AND" SPLITTER
    # =================================================

    def _split_and(self, text):

        matches = list(
            re.finditer(
                r"\s+and\s+",
                text,
                flags=re.IGNORECASE
            )
        )

        if not matches:

            return [text.strip()]

        commands = []

        start = 0

        for match in matches:

            left = text[
                start:match.start()
            ].strip()

            right = text[
                match.end():
            ].strip()

            # Only split when the right side
            # starts another known command.

            if self._starts_command(right):

                if left:

                    commands.append(left)

                start = match.end()

        remaining = text[start:].strip()

        if remaining:

            commands.append(remaining)

        return commands

    # =================================================
    # COMMAND START CHECK
    # =================================================

    def _starts_command(self, text):

        text = text.lower().strip()

        for starter in self.COMMAND_STARTERS:

            if text.startswith(starter):

                return True

        return False