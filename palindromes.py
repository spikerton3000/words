import load_dictionary
word_list = load_dictionary.load('words.txt')
pali_list = []

for word in word_list:
    if word == word[::-1]:
        pali_list.append(word)

print(f"\nNumber of palindromes found = {len(pali_list)}")
print(*pali_list, sep='\n')