from core.engine import Engine

engine = Engine()

while True:

    text = input("KRUGER > ")

    if text == "exit":
        break

    result = engine.process(text)

    print(result)