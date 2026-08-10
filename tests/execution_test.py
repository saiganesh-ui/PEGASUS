from modules.execution.planner import ExecutionPlanner
from modules.execution.executor import Executor

planner = ExecutionPlanner()
executor = Executor()

decisions = [

    {
        "intent": "open",
        "entity": {"app": "chrome"}
    },

    {
        "intent": "close",
        "entity": {"app": "chrome"}
    },

    {
        "intent": "focus",
        "entity": {"app": "chrome"}
    },

    {
        "intent": "restart",
        "entity": {"app": "chrome"}
    }

]

for decision in decisions:

    print("=" * 50)

    task = planner.plan(decision)

    result = executor.execute(task)

    print(result.message)