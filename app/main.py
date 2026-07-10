"""
Project PEGASUS
Entry Point
"""

from .kruger import Kruger


def main():

    ai = Kruger()

    ai.startup()


if __name__ == "__main__":
    main()