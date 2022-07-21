from random import choice as pick_rand, randint as gen_ind

def get_key(): # list of (<char>, <morse_string>)
    key = []
    with open("key.txt") as f:
        for line in f.readlines():
            char = line[0]
            morse_string = line[2:]

            if morse_string[-1] == '\n':
                morse_string = morse_string[:-1]

            key.append((char, morse_string))
    return key

def main():
    key = get_key()
    inp = ""
    while inp.lower() not in ("exit", "quit", "break"):
        pair = pick_rand(key)
        q_ind = gen_ind(0, 1)

        print(pair[q_ind])
        inp = input("answer: ")

        if inp.lower() == pair[not q_ind]:
            print("correct")
        else:
            print(pair[not q_ind])
        print()

if __name__ == '__main__':
    main()
