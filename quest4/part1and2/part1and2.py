import pathlib

with open(pathlib.Path(__file__).parent / "example.txt") as inf:
    nails = [int(n.strip()) for n in inf.readlines()]

height = min(nails)
solution = sum(n - height for n in nails)

print(solution)
