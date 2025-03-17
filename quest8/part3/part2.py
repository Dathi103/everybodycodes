import pathlib


def main():
    with open(pathlib.Path(__file__).parent / "notes.txt") as inf:
        n_priests = int(inf.read().strip())

    blocks_needed = 0
    tower = [1]
    thickness = 1
    n_acolytes = 5
    n_blocks = 160

    while n_blocks > blocks_needed:
        thickness = ((thickness * n_priests) % n_acolytes) + n_acolytes
        tower = [thickness] + [n + thickness for n in tower] + [thickness]
        removed = (n_priests * len(tower)) * tower[len(tower) // 2] % n_acolytes
        for col in tower[1 : len(tower) // 2]:
            removed += ((n_priests * len(tower)) * col % n_acolytes) * 2

        blocks_needed = sum(tower) - removed

    print(blocks_needed - n_blocks)


if __name__ == "__main__":
    main()
