import pathlib
from statistics import median_low

with open(pathlib.Path(__file__).parent / "example.txt") as inf:
    nails = [int(n.strip()) for n in inf.readlines()]

height = median_low(nails)
solution = sum(abs(n - height) for n in nails)

print(solution)
