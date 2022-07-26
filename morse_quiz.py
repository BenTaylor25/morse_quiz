from typing import Callable, List, Tuple
from random import choice, randint
from colorama import init, Fore, Style
init(convert=True)

def get_key() -> List[Tuple[str, str]]:
    key = []
    with open("key.txt") as f:
        for line in f.readlines():
            char = line[0]
            morse_string = line[2:]

            if morse_string[-1] == '\n':
                morse_string = morse_string[:-1]

            key.append((char, morse_string))
    return key

def get_conversion_mode() -> Callable[[None], int]:
    print("1. Both")
    print("2. Morse to English")
    print("3. English to Morse")

    while True:
        mode = input("mode: ")
        if mode in ("1", "2", "3"):
            break
    print()
    
    if mode == "1":
        return lambda : randint(0, 1)
    return lambda : not int(mode)-2

def main():
    conversion_mode = get_conversion_mode()
    key = get_key()
    while True:
        pair = choice(key)
        q_ind = conversion_mode()

        print(pair[q_ind])
        inp = input("answer: ")

        answered_correctly = inp.lower() == pair[not q_ind]
        if answered_correctly:
            print(Fore.GREEN + "correct" + Style.RESET_ALL)
        else:
            print(Fore.RED + pair[not q_ind] + Style.RESET_ALL)
        print()

        # repeat until
        if inp.lower() in ("exit", "quit", "break", "close"):
            break

if __name__ == '__main__':
    main()
