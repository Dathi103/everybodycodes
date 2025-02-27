import pathlib
from itertools import cycle

with open(pathlib.Path(__file__).parent / "example.txt") as inf:
    notes = inf.read()

values = {"=": 0, "-": -1, "+": 1}

d = {
    plan: [values[action] for _, action in zip(range(10), cycle(actions.split(",")))]
    for plan, actions in [line.split(":") for line in notes.split("\n")]
}

sums = {}
for name, values in d.items():
    strength = 10
    total = 0
    for v in values:
        strength += v
        total += strength
    sums[name] = total

print("".join(sorted(sums, key=lambda p: sums[p], reverse=True)))
