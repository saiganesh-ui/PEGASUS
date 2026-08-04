"""
Scheduler
Project PEGASUS
"""

from datetime import datetime
from modules.database.reminder_repository import ReminderRepository


class Scheduler:

    def __init__(self):

        self.tasks = []

        self.repository = ReminderRepository()

    def add(self, task):

        self.repository.save(task)

        self.tasks.append(task)
    def get_due(self):

        now = datetime.now()

        due = []
        pending = []

        for task in self.tasks:

            if task.execute_at <= now:
                due.append(task)
            else:
                pending.append(task)

        self.tasks = pending

        return due
    
    def load_saved_tasks(self):

        tasks = self.repository.load_pending()

        for task in tasks:
            self.tasks.append(task)

        print(f"✓ Loaded {len(tasks)} pending reminders.")