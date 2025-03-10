import pathlib


def main():
    with open(pathlib.Path(__file__).parent / 'notes.txt') as inf:
        n_blocks = int(inf.read().strip())

    blocks_needed = 1
    width = 0

    while n_blocks > blocks_needed:
        if blocks_needed == 1:
            width += 1
        else:
            width += 2
        
        n_blocks -= blocks_needed
        blocks_needed += 2

    result = (width + 2) * (blocks_needed - n_blocks)

    print(result)

if __name__ == "__main__":
    main()