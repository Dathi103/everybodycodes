import pathlib

if __name__ == "__main__":
    filename = 'example.txt'
    with open(pathlib.Path(__file__).parent / filename) as inf:
        notes = inf.readlines()
    
    words = (
        notes[0]
        .removeprefix('WORDS:')
        .strip()
        .split(',')
    )

    inscription = notes[2]

    print(sum(map(inscription.count, words)))

    

