"""
game target
"""
def generate_grid():
    """
    function which generate field with 5 letters
    >>> 1 == 1
    True
    """
    import random
    alp = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    game_field = []
    while len(game_field) < 5:
        a_ch = alp[random.randint(0, 32)]
        if a_ch not in game_field:
            game_field.append(a_ch)
    return game_field

def get_words(f_a, letters):
    """
    function which make a list from file with words
    >>> get_words('base.lst', ['щ'])
    [('щасні', 'noun'), ('щасно', 'adverb'), ('щастя', 'noun'), ('ще', 'adverb'), ('щебет', 'noun'), ('щем', 'noun'), ('щемно', 'adverb'), ('щеня', 'noun'), ('щепа', 'noun'), ('щерба', 'noun'), ('щигля', 'noun'), ('щипак', 'noun'), ('щипок', 'noun'), ('щипці', 'noun'), ('щир', 'noun'), ('щирий', 'adjective'), ('щит', 'noun'), ('щиток', 'noun'), ('щі', 'noun'), ('щіпка', 'noun'), ('щітка', 'noun'), ('щіть', 'noun'), ('щічка', 'noun'), ('щогла', 'noun'), ('щодва', 'adverb'), ('щодві', 'adverb'), ('щодня', 'adverb'), ('щока', 'noun'), ('щоніч', 'adverb'), ('щораз', 'adverb'), ('щорік', 'adverb'), ('щотри', 'adverb'), ('щука', 'noun'), ('щуп', 'noun'), ('щупак', 'noun'), ('щупик', 'noun'), ('щупля', 'noun'), ('щур', 'noun'), ('щурик', 'noun'), ('щурка', 'noun'), ('щуря', 'noun'), ('щучий', 'adjective'), ('щучин', 'adjective'), ('щучка', 'noun')]
    """
    list_of_tuples = []
    with open(f_a, 'r', encoding='utf-8') as file:
        for line in file:
            ls_st = line.split()
            for i in ls_st:
                if len(ls_st[0]) <= 5 and ls_st[0][0] in letters:
                    if 'noun' in i or '/n' in i:
                        list_of_tuples.append((ls_st[0], 'noun'))
                        break
                    if 'adj' in i:
                        list_of_tuples.append((ls_st[0], 'adjective'))
                        break
                    if 'adv' in i and not 'advp' in i:
                        list_of_tuples.append((ls_st[0], 'adverb'))
                        break
                    if 'verb' in i or '/v' in i:
                        list_of_tuples.append((ls_st[0], 'verb'))
                        break
    return list_of_tuples

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    function which return 2 lists with nown and unnown words
    >>> check_user_words([], "adverb", ['ш', 'ь', 'т', 'і', 'х'],get_words('base.lst', ['ш', 'ь', 'т', 'і', 'х']))
    ([], ['ізнов', 'інак', 'інако', 'інде', 'іноді', 'іще', 'тамки', 'темно', 'тепер', 'тепло', 'тихо', 'тихше', 'тоді', 'торік', 'точно', 'тричі', 'трохи', 'туго', 'туди', 'тудою', 'тужно', 'тут', 'тутки', 'тюпки', 'тяжко', 'хапко', 'хибко', 'хижо', 'хирно', 'хитро', 'хмуро', 'хором', 'худо', 'хутко', 'шумко', 'шумно'])
    """
    cor_use_words1 = []
    for i in range(len(user_words)):
        if user_words[i][0] in letters:
            cor_use_words1.append(user_words[i])
    cor_use_words2 = []

    for i in range(len(cor_use_words1)):
        for j in range(len(dict_of_words)):
            if cor_use_words1[i] == dict_of_words[j][0] and dict_of_words[j][1] == language_part:
                cor_use_words2.append((cor_use_words1[i]))
    non_find_words = []
    for i in range(len(dict_of_words)):
        if dict_of_words[i][1] == language_part and dict_of_words[i][0] not in cor_use_words2:
            non_find_words.append(dict_of_words[i][0])

    return cor_use_words2, non_find_words

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())


