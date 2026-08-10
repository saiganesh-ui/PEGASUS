"""
Project PEGASUS
Entry Point
"""

from .kruger import Kruger
from skills.open_skill import OpenSkill


def main():

    ai = Kruger()

    ai.startup()


if __name__ == "__main__":
    main()

    skill = OpenSkill()

    decision = {
        "intent": "open",
        "target": "notepad"
    }

    print(skill.execute(decision))