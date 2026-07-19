from .intent_router import IntentRouter


router = IntentRouter()


def greet():

    return "Hello, Ganesh."


def status():

    return "I'm operating normally."


router.register(
    "greeting",
    greet
)

router.register(
    "status",
    status
)

print(
    router.dispatch("greeting")
)

print(
    router.dispatch("status")
)