import itertools
from pathlib import Path
from typing import Iterable

import pytest

test = """199
200
208
210
200
207
240
269
260
263"""


def increases(entries: Iterable[int]) -> int:
    """"""
    count = 0
    for x, y in zip(entries, entries[1:]):
        if y > x:
            count += 1
    return count


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 7),
        (Path("input01.txt").read_text().strip(), 1759),
    ),
)
def test_increases(input, expected: int) -> None:
    test_entries = [int(x) for x in input.split()]
    assert increases(test_entries) == expected


def increases3(entries: Iterable[int]) -> int:
    """"""
    count = []
    shift = 0
    for x, y, z in zip(entries[shift:], entries[shift + 1 :], entries[shift + 2 :]):
        count.append(x + y + z)
        shift += 1
    return increases(count)


@pytest.mark.parametrize(
    "input, expected",
    (
        (test, 5),
        (Path("input01.txt").read_text().strip(), 1805),
    ),
)
def test_increases3(input, expected: int) -> None:
    test_entries = [int(x) for x in input.split()]
    assert increases3(test_entries) == expected


if __name__ == "__main__":

    f = Path("input01.txt").read_text().strip().splitlines()
    print(increases([int(x) for x in f]))
    print(increases3([int(x) for x in f]))
