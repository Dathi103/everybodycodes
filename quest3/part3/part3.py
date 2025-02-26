import pathlib


def safe_to_mine(x, y, m):
    return (
        m[x][y] != 0
        and ((x - 1 >= 0) and m[x - 1][y] == m[x][y])
        and ((x + 1 < len(m)) and m[x + 1][y] == m[x][y])
        and ((y - 1 >= 0) and m[x][y - 1] == m[x][y])
        and ((y + 1 < len(m[0])) and m[x][y + 1] == m[x][y])
        and ((x - 1 >= 0 and y - 1 >= 0) and m[x - 1][y - 1] == m[x][y])
        and ((x + 1 < len(m) and y - 1 >= 0) and m[x + 1][y - 1] == m[x][y])
        and ((x - 1 >= 0 and y - 1 < len(m[0])) and m[x - 1][y + 1] == m[x][y])
        and ((x - 1 < len(m) and y - 1 < len(m[0])) and m[x + 1][y + 1] == m[x][y])
    )


if __name__ == "__main__":
    filename = "example.txt"
    with open(pathlib.Path(__file__).parent / filename) as inf:
        minemap = inf.read()

    minemap = [[1 if c == "#" else 0 for c in line] for line in minemap.split("\n")]

    while True:
        old_map = [[i for i in line] for line in minemap]
        for x, line in enumerate(old_map):
            for y, n in enumerate(line):
                if safe_to_mine(x, y, old_map):
                    minemap[x][y] += 1
        if minemap == old_map:
            break

    print(sum(sum(line) for line in minemap))

    for line in minemap:
        print("".join("." if n == 0 else str(n) for n in line))
