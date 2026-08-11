"""
Executor
Project PEGASUS
Author: Sai Ganesh
"""

from modules.execution.action_result import ActionResult


class Executor:

    def execute(self, task):

        result = ActionResult()

        result.action = task.intent
        result.target = task.target

        print(f"\nExecuting task: {task.intent}")

        for step in task.steps:

            print(f" -> {step}")

            if step == "validate":

                if not task.target:

                    result.success = False
                    result.message = "Validation failed."
                    return result

            elif step == "open":

                from modules.actions.open_action import OpenAction

                app = task.target.get("app", "").strip()

                if not app:

                    result.success = False
                    result.message = "I couldn't identify which application you want to open."
                    return result

                action = OpenAction()

                success, message = action.execute(app)

                if not success:

                    result.success = False
                    result.message = message
                    return result

                result.message = message
                
            elif step == "close":

                from modules.actions.close_action import CloseAction

                action = CloseAction()

                action.execute(task.target["app"])

            elif step == "focus":

                from modules.actions.focus_action import FocusAction

                action = FocusAction()

                action.execute(task.target["app"])

            elif step == "wait":

                import time

                time.sleep(2)

            elif step == "verify":

                print("Verifying...")

        result.success = True

        if not result.message:
            result.message = f"{task.intent.capitalize()} plan executed."

        return result