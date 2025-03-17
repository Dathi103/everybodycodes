import pathlib


if __name__ == "__main__":
    filename = "example.txt"
    with open(pathlib.Path(__file__).parent / filename) as infile:
        seq = infile.read().strip()
        duels = [seq[i] + seq[i + 1] for i in range(0, len(seq), 2)]

        potions = {"A": 0, "B": 1, "C": 3, "D": 5}

        solution = sum(
            potions.get(a, 0) + potions.get(b, 0) + bool(a != "x" and b != "x") * 2
            for a, b in duels
        )

        print(solution)
