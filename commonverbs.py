import ast
import os

from commonverbs_helpers import flat, is_function_builtin, get_verbs_from_string, get_top_words


def make_files_list(path=''):
    files_list = []
    for dir_name, dirs, files in os.walk(path, topdown=True,):
        for file_name in files:
            if file_name.endswith('.py'):
                files_list.append(os.path.join(dir_name, file_name))
    return files_list


def make_ast_trees(files_list, with_filenames=False, with_filecontent=False):
    trees = []
    for file_name in files_list:
        with open(file_name, 'r', encoding='utf-8') as attempt_handler:
            file_content = attempt_handler.read()
        try:
            tree = ast.parse(file_content)
        except Exception as e:
            print(e)
            tree = None
        if with_filenames:
            if with_filecontent:
                trees.append(file_name, file_content, tree)
            else:
                trees.append(file_name, tree)
        else:
            trees.append(tree)
    return trees


def make_trees_from_path(path, with_filenames=False, with_filecontent=False):
    files_list = make_files_list(path, with_filenames, with_filecontent)
    return make_ast_trees(files_list)


def get_functions_names(tree):
    return [node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]


def get_variables_names(tree):
    return [node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_top_verbs_in_path(path, with_filenames=False, with_filecontent=False, top_size=10):
    files_list = make_files_list(path)
    ast_trees = make_ast_trees(files_list, with_filenames, with_filecontent)
    all_function_names = flat(get_functions_names(tree) for tree in ast_trees)
    all_verbs = flat([get_verbs_from_string(name) for name in all_function_names if not is_function_builtin(name)])
    return get_top_words(all_verbs, top_size)

if __name__ == '__main__':
    Path = '/Users/mentat_ij/otus_task_01/venv/lib/python3.6/site-packages/requests'
    print(get_top_verbs_in_path(Path))


