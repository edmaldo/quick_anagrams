
"""Using a txt file of 45,000+ words, the program displays a list of words that can be used
to build an anagram from a name entered by the user"""

import sys
from collections import Counter
import load_list

dict_file = load_list.load('words.txt')
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)

print("Lets create an anagram of any given name!\n")
given_name = input("Enter a name: ")


def find_anagrams(name, word_list):
    """Read name and dictionary file and display all anagrams in name"""
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)

    print("\nWords left to choose from: ")
    print(*anagrams, sep='\n')
    print(f"\nRemaining letters = {name}")
    print(f"Remaining letters = {len(name)}")
    print(f"Remaining anagrams = {len(anagrams)}")


def process_choice(name):
    """Check user choice for validity, return choice and leftover letters"""
    while True:
        choice = input("\nChoose word to add: ")
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break

        print("Won't work, make another choice.")
    name = ''.join(left_over_list)
    return choice, name


def main():
    """Help the user build anagram from their name"""
    name = ''.join(given_name.lower().split())
    name = name.replace('-', '')
    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            find_anagrams(name, dict_file)
            print(f"Current anagram phrase = {phrase}")

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print("\n******** FINISHED! ********\n")
            print(f"Anagram of {given_name} = {phrase}")
            try_again = input("\nTry this name again? [yes, press 'enter'] [exit, type 'x']: ")
            if try_again.lower() == "x":
                sys.exit()
            else:
                main()


if __name__ == '__main__':
    main()
