import itertools
import math
import sys
from typing import Iterable, Set, Union


def get_ints_from_input(count: int) -> Iterable[int]:
    """Read a single line from input and map it to int. Expects a space seperated list of values. Raises error."""
    ints = map(int, input().split(" "))
    elements: int = 0

    while True:
        try:
            value: int = next(ints)
            elements += 1
            if elements > count:
                break
            yield value
        except StopIteration:
            break

    if elements != count:
        raise ValueError("Invalid input, too many or too few values provided!")


def calculate_distance() -> int:
    n: int
    m: int
    n, m = get_ints_from_input(2)
    setA: Set[int] = set(get_ints_from_input(n))
    setB: Set[int] = set(get_ints_from_input(m))

    # return early if there's common element
    if setA.intersection(setB):
        return 0

    minimum: Union[int, None] = None
    valA: int
    valB: int
    for valA, valB in itertools.product(setA, setB):
        distance: int = abs(valA - valB)
        if minimum is None or minimum > distance:
            minimum = distance

    return minimum


if __name__ == "__main__":
    try:
        result = calculate_distance()
        print(result)
    except (ValueError, EOFError) as err:
        print(err)
        sys.exit(1)
