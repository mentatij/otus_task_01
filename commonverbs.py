import ast
import os

from commonverbs_helpers import make_lat, is_function_builtin, get_verbs_from_string, get_top_words


def make_files_list(path=''):
    if os.path.isfile(path):
        return [path]
    files_list = []
    for dir_name, dirs, files in os.walk(path, topdown=True,):
        for file_name in files:
            if file_name.endswith('.py'):
                files_list.append(os.path.join(dir_name, file_name))
    return files_list


def make_ast_trees_from_files_list(files_list, with_filenames=False, with_filecontent=False):
    if not files_list:
        return []
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


def make_ast_trees_from_path(path, with_filenames=False, with_filecontent=False):
    files_list = make_files_list(path)
    return make_ast_trees_from_files_list(files_list, with_filenames, with_filecontent)


def get_functions_names(tree):
    return [node.name.lower() for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]


def get_variables_names(tree):
    return [node.id.lower() for node in ast.walk(tree) if isinstance(node, ast.Name)]


def fetch_top_verbs_in_path(path='', top_size=10, with_filenames=False, with_filecontent=False):
    ast_trees = make_ast_trees_from_path(path, with_filenames, with_filecontent)
    functions_names = make_lat(get_functions_names(tree) for tree in ast_trees)
    all_verbs = make_lat([get_verbs_from_string(name) for name in functions_names if not is_function_builtin(name)])
    return get_top_words(all_verbs, top_size)


if __name__ == '__main__':
    projects_folder_path = '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages'
    projects = [
        'flask',
        'Django',
        'requests',
        'setuptools',
        'sqlalchemy',
         ]
    top_size = 5

    for project in projects:
        project_path = os.path.join(projects_folder_path, project)
        if os.path.exists(project_path):
            print('Project "%s" found.' % project)
            print('The %d most used verbs in the project are:' % top_size)
            print(fetch_top_verbs_in_path(project_path, top_size))
        else:
            print('Project %s not found.' % (project))
        print('-' * 60)
