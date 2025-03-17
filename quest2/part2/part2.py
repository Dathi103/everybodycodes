import pathlib
from time import perf_counter

if __name__ == "__main__":
    filename = "example.txt"
    with open(pathlib.Path(__file__).parent / filename) as inf:
        notes = inf.readlines()
    words = notes[0].removeprefix("WORDS:").strip().split(",")
    words.extend([word[::-1] for word in words])
    words = set(words)

    lines = [line.strip() for line in notes[2:]]

    num_symbols = 0

    for line in lines:
        indices = set()
        for i in range(len(line)):
            for word in words:
                if line[i : i + len(word)] == word:
                    for ix in range(i, i + len(word)):
                        indices.add(ix)
        num_symbols += len(indices)

    print(num_symbols)
