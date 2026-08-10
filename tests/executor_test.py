from modules.execution.planner import ExecutionPlanner
from modules.execution.executor import Executor

planner = ExecutionPlanner()
executor = Executor()

decision = {
    "intent": "restart",
    "entity": {"app": "chrome"}
}

task = planner.plan(decision)

result = executor.execute(task)

print("\nSuccess :", result.success)
print("Message :", result.message)