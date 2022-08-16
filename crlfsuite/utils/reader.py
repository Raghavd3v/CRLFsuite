# -*- coding: utf-8 -*-

def reader(file):
    """
    reads a file and returns its content
    """
    with open(file, 'r', encoding='utf-8') as _file:
        read = _file.read().splitlines()

    return read