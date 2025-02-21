import pathlib


if __name__ == "__main__":
    filename = 'example.txt'
    with open(pathlib.Path(__file__).parent / filename) as inf:
        seq = inf.read().strip()
        
    fights = [seq[i:i+3] for i in range(0, len(seq), 3)]

    potions = {
        'A': 0,
        'B': 1,
        'C': 3,
        'D': 5
    }

    extra = {
        0: 6,
        1: 2,
    }

    solution = sum(
        sum(potions.get(f, 0) for f in fight)
        + extra.get(fight.count('x'), 0)
        
        for fight
        in fights
    )

    print(solution)