import collections

from nltk import pos_tag


def make_lat(arg_list):
    """[(1, 2), (3, 4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in arg_list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']  # or == 'VB' ?


def is_function_builtin(function_name):
    return function_name.startswith('__') and function_name.endswith('__')


def split_snake_case(name):
    return [n for n in name.split('_') if n]


def get_verbs_from_string(some_string):
    return [word for word in some_string.split('_') if is_verb(word)]


def get_top_words(words_list, top_size=10):
    return collections.Counter(words_list).most_common(top_size)
