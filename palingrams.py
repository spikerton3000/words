import load_dictionary
word_list = load_dictionary.load('words.txt')


def find_palingrams():
    palingram_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[1:] == rev_word[:end-i] and rev_word[end-1:] in word_list:
                    palingram_list.append((word, rev_word[end-1:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    palingram_list.append((rev_word[:end-i], word))

    return palingram_list

palingrams = find_palingrams()

print(f"\n Number of palingrams = {len(palingrams)}\n")
for first, second in palingrams:
    print(f"{first} {second}")