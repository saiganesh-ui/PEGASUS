"""
Time Parser
Project PEGASUS
"""

from datetime import datetime, timedelta


class TimeParser:

    def parse(self, delay, unit):

        unit = unit.lower()

        if unit.startswith("second"):
            return datetime.now() + timedelta(seconds=delay)

        if unit.startswith("minute"):
            return datetime.now() + timedelta(minutes=delay)

        if unit.startswith("hour"):
            return datetime.now() + timedelta(hours=delay)

        if unit.startswith("day"):
            return datetime.now() + timedelta(days=delay)

        return datetime.now()