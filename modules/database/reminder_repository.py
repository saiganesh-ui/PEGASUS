"""
Reminder Repository
Project PEGASUS
"""

from datetime import datetime
from modules.memory.database import Database
from modules.scheduler.task import Task



class ReminderRepository:

    def __init__(self):

        self.db = Database()

    def save(self, task):

        self.db.cursor.execute("""

        INSERT INTO reminders(command, execute_at)

        VALUES(?,?)

        """, (

            task.command,

            task.execute_at.isoformat()

        ))

        self.db.connection.commit()

        print("Saved reminder:", task.command)

    def load(self):

        self.db.cursor.execute("""

        SELECT id, command, execute_at

        FROM reminders

        """)

        rows = self.db.cursor.fetchall()

        reminders = []

        for row in rows:

            reminders.append(

                Task(

                    id=row[0],

                    command=row[1],

                    execute_at=datetime.fromisoformat(row[2])

                )

            )

        return reminders

    def delete(self, reminder_id):
    
            self.db.cursor.execute(
                "DELETE FROM reminders WHERE id = ?",
                (reminder_id,)
            )
    
            self.db.connection.commit()

    def get_all(self):

        self.db.cursor.execute("""
            SELECT command, execute_at
            FROM reminders
        """)

        return self.db.cursor.fetchall()  

    def load_pending(self):

        self.db.cursor.execute("""
            SELECT id, command, execute_at
            FROM reminders
        """)

        rows = self.db.cursor.fetchall()

        tasks = []

        for row in rows:

            tasks.append(
                Task(
                    id=row[0],
                    command=row[1],
                    execute_at=datetime.fromisoformat(row[2])
                )
            )

        return tasks  

    