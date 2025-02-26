import pathlib

with open(pathlib.Path(__file__).parent / "example.txt") as inf:
    lines = [list(map(int, line.strip().split())) for line in inf.readlines()]

columns = [list(col) for col in zip(*lines)]

current_col = 0
num_rounds = 0
counter = {}

while True:
    num_rounds += 1
    clapper = columns[current_col].pop(0)
    target_column = (current_col + 1) % len(columns)
    side, ix = divmod(clapper - 1, len(columns[target_column]))
    ix = len(columns[target_column]) - ix if side % 2 else ix
    columns[target_column].insert(ix, clapper)
    current_col = target_column
    number = int("".join([str(col[0]) for col in columns]))
    counter[number] = counter.get(number, 0) + 1
    print(columns)
    if counter[number] == 2024:
        print(number * num_rounds)
        break
