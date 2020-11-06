"""Find palindromic pairs from 45,000+ items in the words.txt file."""

import load_list

word_list = load_list.load('words.txt')


def find_palindromes():
    """Find dictionary palindromes"""
    palin_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    palin_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    palin_list.append((rev_word[:end-i], word))
    return palin_list


palindromes = find_palindromes()
palindromes_sorted = sorted(palindromes)

for first, second in palindromes_sorted:
    print(f"{first} {second}")
print(f"\nNumber of palindromic pairs = {len(palindromes_sorted)}\n")