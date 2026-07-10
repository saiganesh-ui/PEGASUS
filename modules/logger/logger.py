"""
KRUGER Logger
Project PEGASUS
"""

from datetime import datetime


class Logger:

    def __init__(self):

        self.log_file = "logs/kruger.log"

    def info(self, message):

        self.write("INFO", message)

    def error(self, message):

        self.write("ERROR", message)

    def write(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        line = f"[{timestamp}] [{level}] {message}\n"

        with open(self.log_file, "a", encoding="utf-8") as file:

            file.write(line)