"""Solve the 'Infinite House of Pancakes' problem.

https://code.google.com/codejam/contest/6224486/dashboard#s=p1
"""
from solver import solver


def cost(n, l):
    q, r = divmod(n, l)
    return q + bool(r) - 1


def test(s, l):
    return l + sum(cost(x, l) for x in s)


def solve(s):
    return min(test(s, l) for l in xrange(1, max(s)+1))


@solver(case_width=2)
def pancake(lines):
    arg = map(int, lines[1].split())
    return solve(arg)

if __name__ == "__main__":
    pancake.from_cli()
