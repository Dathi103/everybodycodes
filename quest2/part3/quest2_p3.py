import pathlib
from time import perf_counter

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
    words.extend([word[::-1] for word in words])
    words = set(words)

    lines = [line.strip() for line in notes[2:]]
    lines_t = [''.join(chars) for chars in zip(*lines)]

    indices = set()

    for x, line in enumerate(lines):
        for i in range(len(line)):
            for word in words:
                if line[i:i+len(word)] + line[:(i+len(word))%len(line)] * (i + len(word) > len(line)) == word:
                    for y in range(i, i+len(word)):
                        indices.add((x, y % len(line)))

    for x, line in enumerate(lines_t):
        for i in range(len(line)):
            for word in words:
                if line[i:i+len(word)] == word:
                    for y in range(i, i+len(word)):
                        indices.add((y, x))

    

    print(len(indices))

    







    

