import itertools
from pathlib import Path
from typing import Callable, Iterable

import pytest

test = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def forward(amount, horizontal, vertical):
    return horizontal + amount, vertical


def up(amount, horizontal, vertical):
    return horizontal, vertical - amount


def down(amount, horizontal, vertical):
    return horizontal, vertical + amount


ACTION_MAP: dict[str, Callable] = {
    "forward": forward,
    "up": up,
    "down": down,
}


def forward_aim(amount, horizontal, vertical, aim):
    return horizontal + amount, vertical + aim * amount, aim


def up_aim(amount, horizontal, vertical, aim):
    return horizontal, vertical, aim - amount


def down_aim(amount, horizontal, vertical, aim):
    return horizontal, vertical, aim + amount


ACTION_MAP2: dict[str, Callable] = {
    "forward": forward_aim,
    "up": up_aim,
    "down": down_aim,
}


def parse_commands(entries: Iterable) -> dict:
    d = []
    for line in entries.splitlines():
        command, _, value = line.partition(" ")
        d.append((command, int(value)))
    return d


def main(commands_raw):
    h = v = 0
    commands = parse_commands(commands_raw)
    for com, amount in commands:
        h, v = ACTION_MAP[com](amount, h, v)

    return h * v


def main2(commands_raw):
    h = v = a = 0
    commands = parse_commands(commands_raw)
    for com, amount in commands:
        h, v, a = ACTION_MAP2[com](amount, h, v, a)

    return h * v


if __name__ == "__main__":
    f = Path("input02.txt").read_text().strip()
    print(main(test))
    print(main(f))  # 1451208
    print(main2(test))
    print(main2(f))  # 1620141160
