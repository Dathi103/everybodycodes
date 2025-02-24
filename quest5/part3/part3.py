import pathlib

with open(pathlib.Path(__file__).parent / 'example.txt') as inf:
    lines = [
        list(map(int, line.strip().split())) 
        for line in inf.readlines()
    ]

columns = [list(col) for col in zip(*lines)]

current_col = 0
num_rounds = 0
counter = {}
snapshots = []
shouts = set()

while True:
    num_rounds += 1
    clapper = columns[current_col].pop(0)
    target_column = (current_col + 1) % len(columns)
    side, ix = divmod(clapper - 1, len(columns[target_column]))
    ix = len(columns[target_column]) - ix if side % 2 else ix
    columns[target_column].insert(ix, clapper)
    current_col = target_column
    number = int(''.join([str(col[0]) for col in columns]))

    new_snapshot = [[n for n in col] for col in columns]

    if not any(new_snapshot == snapshot for snapshot in snapshots):
        snapshots.append(new_snapshot)
        shouts.add(number)
        if num_rounds % 10000 == 0:
            print(num_rounds, len(snapshots))
    else:
        print(max(shouts))
        break


    