from modules.execution.planner import ExecutionPlanner

planner = ExecutionPlanner()

commands = [

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

for decision in commands:

    task = planner.plan(decision)

    print("=" * 40)
    print("Intent :", task.intent)
    print("Target :", task.target)
    print("Steps  :", task.steps)