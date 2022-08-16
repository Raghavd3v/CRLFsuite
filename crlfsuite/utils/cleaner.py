# -*- coding: utf-8 -*-

import os

def clean():
    """
    removes all the CRLFsuite generated files from the current path
    """
    if os.path.isfile('resumable_data.crlfsuite'):
        os.remove('resumable_data.crlfsuite')
    else:
        None
    if os.path.isfile('resume.cfg'):
        os.remove('resume.cfg')
    else:
        None