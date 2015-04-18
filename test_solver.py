"""Provide tests for the solver."""

# Imports
import os
from example.pancake import pancake
from pytest import yield_fixture, main

# Constants
BASE = "example/B-large-practice"
INPUT = BASE + ".in"
OUTPUT = BASE + ".out"
EXPECTED = OUTPUT + ".expected"


@yield_fixture(params=[True, False],
               ids=["with multiprocessing", "without multiprocessing"])
def solve_pancake(request):
    pancake(INPUT, multiprocessing=request.param)
    yield open(OUTPUT).read()
    os.remove(OUTPUT)


def test_pancake(solve_pancake):
    assert solve_pancake == open(EXPECTED).read()

# Main execution
if __name__ == "__main__":
    main()
