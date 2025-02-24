import pathlib

with open(pathlib.Path(__file__).parent / 'example.txt') as inf:
    lines = [
        list(map(int, line.strip().split())) 
        for line in inf.readlines()
    ]

columns = [list(col) for col in zip(*lines)]

num_rounds = 10
current_col = 0

for _ in range(num_rounds):
    clapper = columns[current_col].pop(0)
    target_column = (current_col + 1) % len(columns)
    side, ix = divmod(clapper - 1, len(columns[target_column]))

    ix = len(columns[target_column]) - 1 - ix if side % 2 else ix

    columns[target_column].insert(ix, clapper)

    current_col = target_column

print(''.join([str(col[0]) for col in columns]))
    