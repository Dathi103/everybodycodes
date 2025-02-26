import pathlib


if __name__ == "__main__":
    filename = "example.txt"
    with open(pathlib.Path(__file__).parent / filename) as inf:
        seq = inf.read().strip()

    req_potions = {"A": 0, "B": 1, "C": 3}

    solution = sum(req_potions[c] for c in seq)

    print(solution)
