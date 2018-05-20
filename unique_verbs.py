import ast
import collections
import os

from nltk import pos_tag


def flat_list(arg_list):
    """Converts [(1, 2), (3, 4)] to [1, 2, 3, 4]"""
    return sum([list[item] for item in arg_list], [])


def is_verb(word):
    pos_info = pos_tag(word)
    return pos_info[0][1] in ['VB', 'VBP']# or == 'VB'


def make_files_list(path=''):
    files_list = []
    for dir_name, dirs, files in os.walk(path, topdown=True,):
        for file_name in files:
            if file_name.endswith('.py'):
                files_list.append(os.path.join(dir_name, file_name))
    return files_list


def make_trees(files_list):
    trees = []
    for file in files_list:
        with open(file, 'r', encoding='utf-8') as attempt_handler:
            file_content = attempt_handler.read()
        try:
            tree = ast.parse(file_content)
        except Exception as e:
            print(e)
        trees.append(tree)
    return trees


def get_names():
    return [node.id for node in ast.walk() if isinstance(node, ast.Name)]  # or ast.FunctionDef may be?


def get_verb_from_name(name):
    return [word for word in name.split('_') if is_verb(word)]





if __name__ == "__main__":
    a = make_files_list('/Users/mentat_ij/otus_task_01/venv/lib/python3.6/site-packages/requests')
    print(len(a))
    b = make_trees(a)
    print(type(b[0]))
    print(b[0].__dict__)
