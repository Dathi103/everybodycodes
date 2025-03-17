import pathlib


def build_tower(thickness, old_tower) -> tuple[dict[int, int], int]:
    new_tower = {}
    needed = 0
    width = old_tower.get(0, -1) + 2
    for i in range(thickness):
        needed += width - old_tower.get(i, 0)
        new_tower[i] = width
    for i in range(len(old_tower)):
        needed += old_tower[i] - old_tower.get(i + thickness, 0)
        new_tower[i + thickness] = old_tower[i]

    return new_tower, needed


def main():
    with open(pathlib.Path(__file__).parent / "notes.txt") as inf:
        n_priests = int(inf.read().strip())

    blocks_needed = 0
    tower = {}
    thickness = 0
    n_acolytes = 5
    n_blocks = 50

    while n_blocks > blocks_needed:
        n_blocks -= blocks_needed
        thickness = (thickness * n_priests) % n_acolytes or 1
        tower, blocks_needed = build_tower(thickness, tower)

    print((blocks_needed - n_blocks) * tower[0])


if __name__ == "__main__":
    main()
