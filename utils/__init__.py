import os
from pathlib import Path


def input_path(file_name):
    return Path(os.getcwd()).parent / "inputs" / file_name


def read_lines(file_name):
    with open(input_path(file_name)) as file:
        return file.readlines()


def is_digit(char):
    return 48 <= ord(char) <= 57
