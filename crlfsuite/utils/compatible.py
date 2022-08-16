# -*- coding: utf-8 -*-

import sys

def compatible_path(path):
    """
    ensures the compatibility with windows
    """
    if sys.platform.lower().startswith('win'):
        return path.replace('/', '\\')
    return path