from tqdm import tqdm

import pathlib
from itertools import cycle, permutations


def calculate_total(plan, track, base_strength=10):
    total = 0
    strength = base_strength
    for v, seg in zip(cycle(plan), track):
        strength += seg or v
        total += strength
    return total


values = {"=": 0, "S": 0, "-": -1, "+": 1}

with open(pathlib.Path(__file__).parent / "track.txt") as inf:
    track_notes = inf.read().split("\n")
with open(pathlib.Path(__file__).parent / "plan.txt") as inf:
    rival_plan = [values[action] for action in inf.read().split(":")[1].split(",")]


max_len = max(map(len, track_notes))
track_grid = [list(line) + [" "] * (max_len - len(line)) for line in track_notes]

track = []
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
prev_x, prev_y = 1, 0
x, y = 0, 0

while True:

    for move_x, move_y in moves:
        new_x = x + move_x
        new_y = y + move_y
        if (
            0 <= new_x < len(track_grid)
            and 0 <= new_y < len(track_grid[0])
            and track_grid[new_x][new_y] != " "
            and (new_x, new_y) != (prev_x, prev_y)
        ):
            prev_x, prev_y = x, y
            x, y = new_x, new_y
            break

    seg = track_grid[x][y]
    track.append(values[seg])

    if seg == "S":
        break

track = track * 11

rival_total = calculate_total(rival_plan, track)

all_plans = set(permutations([1] * 5 + [-1] * 3 + [0] * 3))

better_plans = 0
for plan in tqdm(all_plans):
    total = calculate_total(plan, track)
    if total > rival_total:
        better_plans += 1

print(better_plans)
