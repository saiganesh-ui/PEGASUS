"""
Help Skill
Project PEGASUS
"""

from skills.base_skill import BaseSkill


class HelpSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

    def can_handle(self, decision):

        return decision["intent"] == "help"

    def execute(self, decision):

        text = """
==========================
      KRUGER HELP
==========================

MEMORY
-------
remember github=ganesh348
recall github
forget github
what do you know about me

APPLICATIONS
------------
open chrome
open vscode
open notepad

SEARCH
------
search python
search github

FILES
-----
create folder demo
create file notes.txt
delete file notes.txt
delete folder demo

REMINDERS
---------
remind me to drink water in 5 minutes

SYSTEM
------
status
time
date
day

WEATHER
-------
weather
weather in hyderabad

GENERAL
-------
help
history

==========================
"""

        return {
            "type": "response",
            "message": text
        }