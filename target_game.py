"""
Module hich a game target
"""
from typing import List
import random
import sys
import doctest

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    word_list = []
    for _ in range(9):
        word_list.append(chr(random.randint(97, 122)))
    print(word_list)
    return word_list

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    list_words = []
    with open(f, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            if len(line) >= 4 and (line not in list_words) and letters[4] in line:
                let_in_word = [0]
                let_in_word *= 26
                for i in range(len(line)):
                    if line[i]!='-':
                        let_in_word[ord(line[i]) - 97] += 1
                let = [0]
                let *= 26
                for i in range(9):
                    let[ord(letters[i]) - 97] += 1
                flag_let = True
                for i in range(26):
                    if let_in_word[i] > 0:
                        if let[i] >= let_in_word[i]:
                            continue
                        else:
                            flag_let = False
                            break
                if flag_let == True:
                    list_words.append(line)
    return list_words



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    for line in sys.stdin:
        user_words.append(line[:len(line) - 1])
    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    unnown_list = []
    for i in range(len(user_words)):
        redact_word = user_words[i].lower()
        st_word = user_words[i]
        if redact_word in words_from_dict:
            if redact_word != user_words[i]:
                unnown_list.append(user_words[i].lower())
        else:
            let_in_word = [0]
            let_in_word *= 26
            lenth = len(user_words[i])
            for j in range(lenth):
                let_in_word[ord(redact_word[j]) - 97] += 1
            let = [0]
            let *= 26
            flag = True
            for i in range(len(letters)):
                let[ord(letters[i]) - 97] += 1
            for i in range(26):
                if let_in_word[i] > 0:
                    if let[i] >= let_in_word[i]:
                        continue
                    else:
                        flag = False
            if flag == True and letters[4] in st_word.lower():
                unnown_list.append(st_word.lower())
        print(unnown_list)


def results():
    """
    Results the game
    """
    url = "en.txt"
    letters_list = generate_grid()
    list_words = get_words(url, letters_list)
    user_words = get_user_words()
    print(list_words)
    print(user_words)
    get_pure_user_words(user_words, letters_list, list_words)


if __name__ == '__main__':
    results()