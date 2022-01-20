import os
from contextlib import contextmanager

"""Project file to create 7 in 1 architecture for SASS files management"""


def file_extention(func, *args, **kwargs):
    """Decorates file extention to list of files passed as an argument"""

    def wrapper(func, *args, **kwargs):
        list_names = func
        list_names = [f"{file_name}.{args[0]}" for file_name in list_names]
        return list_names

    return wrapper


@file_extention
def file_list(list_names, extension="py"):
    return list_names


seven_in_one = [
    ["abstract", ["_variables", "_mixins", "_extends", "_functions"]],
    ["base", ["_base", "_animations", "_typography"]],
    ["layout", []],
    ["pages", []],
    ["components", ["_button"]],
    ["themes", []],
]


@contextmanager
def to_dir(dir_name):
    cwd = os.getcwd()
    try:
        os.chdir(dir_name)
        yield
    except FileNotFoundError:
        os.mkdir(dir_name)
        os.chdir(dir_name)
        yield
    finally:
        cwd = os.chdir(cwd)


for each in seven_in_one:
    dir_name = each[0]
    files = file_list(each[1], "scss")

    with to_dir(dir_name):
        [os.mknod(file_name) if not os.listdir().__contains__(file_name) else "" for file_name in files]
