# -*- coding: utf-8 -*-

import sys
from colorama import Fore as clr, Style, Back

if sys.platform.lower().startswith(('os', 'win', 'darwin', 'ios')):
    cyan = green = yellow = red = bright = blue = reset = backred = progress = magenta = ''
else:
    cyan = clr.CYAN
    green = clr.LIGHTGREEN_EX
    yellow = clr.LIGHTYELLOW_EX
    red = clr.RED
    bright = Style.BRIGHT
    blue = clr.BLUE 
    reset = Style.RESET_ALL
    backred = Back.RED
    progress = ("[" + blue + bright +'INF' + reset + "] ")
    magenta = clr.LIGHTMAGENTA_EX

banner = f"""{bright}            ___
          ___H___
 _____ _____[{backred}%{reset}{bright}]_____         _ _       
|     | __  [{backred}\{reset}{bright}]   __|___ _ _|_| |_ ___ 
|   --|    -[{backred}#{reset}{bright}]   __|_ -| | | |  _| -_|
|_____|__|__[{backred};{reset}{bright}]__|  |___|___|_|_| |___|
             V                        v2.5.2
                {reset}({green}\x1B[3mBy Nefcore Security\x1B[0m{reset})
"""

def good(msg):
    """
    if URL is vulnerable
    """
    print("[" + green + bright +'VLN' + reset + '] '+msg)

def bad(msg):
    """
    if URL is not vulnerable
    """
    print("[" + magenta + bright + 'NOT VLN' + reset + '] '+msg)

def error(msg):
    """
    if any error occurs
    """
    print("[" + red + bright + 'ERR' + reset + ']',msg)

def info(msg):
    """
    basic informations
    """
    print("[" + blue + bright +'INF' + reset + "] "+msg)

def warn(msg):
    """
    warnings
    """
    print("[" + yellow + bright +'WRN' + reset + "] "+msg)

def args_info(url, urls, stdin, nout, jout, method, data, cookies, timeout, verify, threads, verbosity, delay):
    """
    Prints information about user supplied arguments
    """
    if url:
        print(':: TARGET     : %s' % url)
    elif urls:
        print(':: TARGET     : %s' % urls) 
    elif stdin:
        print(':: TARGET     : Stdin')
    else:
        print(':: TARGET     : None')
    if nout:
        print(':: OUTPUT     : %s' % nout)
    elif jout:
        print(':: OUTPUT     : %s' % jout)

    print(':: THREADS    : %i' % threads)
    print(':: METHOD     : %s' % method)
    
    if data:
        print(':: DATA       : %s' % data)

    print(':: Delay      : %s' % delay)

    if cookies:
        print(':: COOKIES    : %s' % cookies)
    
    print(':: TIMEOUT    : %i' % timeout)
    
    if verify:
        print(':: VERIFY     : True')
    else:
        print(':: VERIFY     : False')
    if verbosity:
        print(':: Verbosity  : %i' % verbosity)
    print('')