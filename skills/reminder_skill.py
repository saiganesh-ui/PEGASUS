"""
Reminder Skill
Project PEGASUS
"""

from datetime import datetime, timedelta

from skills.base_skill import BaseSkill
from modules.scheduler.task import Task
from modules.nlp.time_parser import TimeParser


class ReminderSkill(BaseSkill):

    def __init__(self, context, scheduler=None):

        super().__init__(context, scheduler)

        self.time_parser = TimeParser()

    def can_handle(self, decision):

        return decision["intent"] == "reminder"

    def execute(self, decision):

        entity = decision["entity"]

        command = entity["task"]
        delay = entity["delay"]
        unit = entity["unit"]

        if unit.startswith("second"):
            delta = timedelta(seconds=delay)

        elif unit.startswith("minute"):
            delta = timedelta(minutes=delay)

        elif unit.startswith("hour"):
            delta = timedelta(hours=delay)

        else:
            delta = timedelta(seconds=delay)

        reminder = Task(
            command=command,
            execute_at = self.time_parser.parse(delay, unit)
        )

        self.scheduler.add(reminder)

        return {
            "type": "response",
            "message": f"Reminder set for {delay} {unit}."
        }