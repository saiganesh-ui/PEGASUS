"""
Background Scheduler
Project PEGASUS
"""

import threading
import time

from modules.scheduler import scheduler, task


class BackgroundScheduler:

    def __init__(self, scheduler):

        self.scheduler = scheduler
        self.running = False

    def start(self):

        self.running = True

        thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        thread.start()

    def run(self):

        while self.running:

            due = self.scheduler.get_due()

            for reminder in due:

                print("\n🔔 KRUGER REMINDER")
                print(reminder.command)
                print()

                # Delete from SQLite after execution
                self.scheduler.repository.delete(reminder.id)

            time.sleep(1)

    def stop(self):

        self.running = False
    