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
    let_list = []
    for _ in range(3):
        for _ in range(3):
            ch = chr(random.randint(97, 122))
            let_list.append(ch)
    print(let_list)
    return let_list

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    list_words = []
    let = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0, 0]
    for i in range(len(letters)):
        let[ord(letters[i]) - 97] += 1
    with open(f, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.lower()
            if len(line) >= 4 and (line not in list_words) and letters[4] in line:
                let_in_word = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0, 0]
                let_in_word *= 26
                for i in range(len(line)):
                    if line[i] != '-' and line[i] != ',':
                        let_in_word[ord(line[i]) - 97] += 1
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
    nown_list = []
    count = 0
    for i in range(len(user_words)):
        st_word = user_words[i]
        if st_word in words_from_dict:
            count += 1
            nown_list.append(st_word)
        else:
            let_in_word = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0, 0]
            lenth = len(user_words[i])
            for j in range(lenth):
                let_in_word[ord(st_word[j]) - 97] += 1
            let = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0, 0]
            flag = True
            for i in range(len(letters)):
                    let[ord(letters[i]) - 97] += 1
            for i in range(26):
                if let_in_word[i] > 0:
                    if let[i] >= let_in_word[i]:
                        continue
                    else:
                        flag = False
            if flag == True and letters[4] in st_word:
                unnown_list.append(st_word)
        for i in range(len(unnown_list)):
            print(unnown_list[i], end = ' ')
    with open('result.txt', 'w') as file:
        file.write(str(count))
        file.write('\n')
    with open('result.txt', 'a') as file:
        for i in words_from_dict:
            file.write(i)
            file.write(' ')
        file.write(('\n'))
    with open('result.txt', 'a') as file:
        for i in words_from_dict:
            if i not in nown_list:
                file.write(i)
                file.write(' ')
        file.write('\n')
    with open('result.txt', 'a') as file:
        for i in unnown_list:
            file.write(i)
            file.write(' ')


def results():
    """
    Results the game
    """
    url = "C:\Програмирование\pycharm\en.txt"
    letters_list = generate_grid()
    list_words = get_words(url, letters_list)
    user_words = get_user_words()
    print(list_words)
    for i in range(len(user_words)):
        print(user_words[i], end = ' ')
    print()
    get_pure_user_words(user_words, letters_list, list_words)


if __name__ == '__main__':
    results()