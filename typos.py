from itertools import product
from keyboard import Keyboard


def brutal_typo_in_word(word):
    keyboard = Keyboard()
    arr = []
    for char in word:
        arr.append([char] + list(keyboard[char].links))
    combinations = product(*arr)
    output = []
    for combination in combinations:
        output.append("".join(combination))
    return output


if __name__ == "__main__":
    k = Keyboard()
    # print (k.keys)
    print(brutal_typo_in_word("piwo"))
