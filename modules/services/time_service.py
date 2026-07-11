"""
Time Service
Project PEGASUS
Author: Sai Ganesh
"""

from datetime import datetime


class TimeService:

    def current_time(self):

        return datetime.now().strftime("%I:%M %p")

    def current_date(self):

        return datetime.now().strftime("%d %B %Y")

    def current_day(self):

        return datetime.now().strftime("%A")