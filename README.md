# Common Verbs

> Check your vocabulary!

Common Verbs is a static analysis tool for python code that shows verbs most common used in functions names.

### Installation

1. clone or download the project and install the requirements:
```zsh
$ git clone https://github.com/mentatij/otus_task_01.git
$ cd otus_task_01
$ pip install -r requirements.txt
```
2. install 'averaged_perceptron_tagger' module for Natural Language Toolkit
```python
>>> import nltk
>>> nltk.dowload()
```

### Example of usage

From python code:
```python
>>> import commonverbs
>>> commonverbs.fetch_top_verbs_in_path('/path/to/python_project_folder/')
[('verb_top_1', amount of use_1), ('verb_top_2', amount of use_2), ...]
```
Аlso you can specify the path to a particular python file.

From command line:

Before usage, edit the value of the variables **path, projects, top_size** in the file **commonverbs.py**, 
specifying the path to your projects folder, names of the projects to be analyzed and the number of output words.
```zsh
$ python3 commonverbs.py
Project "flask" found.
The 5 most used verbs in the project are:
[('get', 31), ('make', 10), ('add', 9), ('find', 6), ('is', 5)]
------------------------------------------------------------
Project "Django" found.
The 5 most used verbs in the project are:
[('get', 992), ('add', 148), ('is', 98), ('has', 75), ('save', 60)]
------------------------------------------------------------
Project "requests" found.
The 5 most used verbs in the project are:
[('get', 22), ('is', 6), ('add', 4), ('find', 2), ('encoding', 2)]
------------------------------------------------------------
Project "setuptools" found.
The 5 most used verbs in the project are:
[('get', 56), ('run', 28), ('finalize', 18), ('initialize', 17), ('find', 15)]
------------------------------------------------------------
Project "sqlalchemy" found.
The 5 most used verbs in the project are:
[('get', 415), ('do', 125), ('is', 90), ('has', 77), ('remove', 56)]
------------------------------------------------------------
```

### Docs
No additional docs, just this README.md

### Contributing

1. Fork it (<https://github.com/mentatij/otus_task_01.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request