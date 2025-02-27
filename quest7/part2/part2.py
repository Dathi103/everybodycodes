import pathlib
from itertools import cycle

with open(pathlib.Path(__file__).parent / "example.txt") as inf:
    notes = inf.read()
with open(pathlib.Path(__file__).parent / "track.txt") as inf:
    track_notes = inf.read().split("\n")

values = {"=": 0, "S": 0, "-": -1, "+": 1}

loops = 10

track = (
    list(
        map(
            lambda seg: values[seg],
            list(track_notes[0][1:])
            + [line[-1] for line in track_notes[1:-1]]
            + list(reversed(track_notes[-1]))
            + [line[0] for line in reversed(track_notes[1:-1])]
            + ["S"],
        )
    )
    * loops
)


d = {
    plan: [
        values[action]
        for _, action in zip(range(len(track) * loops), cycle(actions.split(",")))
    ]
    for plan, actions in [line.split(":") for line in notes.split("\n")]
}

sums = {}
for name, values in d.items():
    strength = 10
    total = 0
    for v, seg in zip(values, track):
        strength += seg or v
        total += strength
    sums[name] = total

print("".join(sorted(sums, key=lambda p: sums[p], reverse=True)))
