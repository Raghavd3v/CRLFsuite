# -*- coding: utf-8 -*-

from colorama import Fore as clr, Style, Back
from crlfsuite.core.config import escape_chars, starting_strings, xss_payloads

cyan = clr.CYAN
green = clr.LIGHTGREEN_EX
yellow = clr.LIGHTYELLOW_EX
red = clr.RED
bright = Style.BRIGHT
blue = clr.BLUE 
reset = Style.RESET_ALL
backred = Back.RED

banner = f"""{bright}            ___
          ___H___
 _____ _____[{backred}%{reset}{bright}]_____         _ _       
|     | __  [{backred}\{reset}{bright}]   __|___ _ _|_| |_ ___ 
|   --|    -[{backred}#{reset}{bright}]   __|_ -| | | |  _| -_|
|_____|__|__[{backred};{reset}{bright}]__|  |___|___|_|_| |___|
             V                        v2.1.2
                {reset}({green}\x1B[3mBy Nefcore Security\x1B[0m{reset})
"""

def good(msg):
    print("[" + green + bright +'VLN' + reset + '] '+msg)

def bad(msg):
    print("[" + clr.LIGHTMAGENTA_EX + bright + 'NOT VLN' + reset + '] '+msg)

def error(msg):
    print("[" + red + bright + 'ERR' + reset + ']',msg)

def info(msg):
    print("[" + blue + bright +'INF' + reset + "] "+msg)

def warn(msg):
    print("[" + yellow + bright +'WRN' + reset + "] "+msg)

def verbosity(msg):
    print("[" + cyan + 'VERBOSE' + reset + "]",msg)

def args_info(url, urls, stdin, output, method, data, cookies, timeout, user_agent, verify, threads):
    if url:
        print(':: TARGET     : %s' % url)
    elif urls:
        print(':: TARGET     : %s' % urls) 
    elif stdin:
        print(':: TARGET     : Stdin')
    else:
        print(':: TARGET     : None')
    
    print(':: OUTPUT     : %s' % output)

    print(':: THREADS    : %i' % threads)
    print(':: METHOD     : %s' % method)
    
    if data:
        print(':: DATA       : %s' % data)

    if cookies:
        print(':: COOKIES    : %s' % cookies)
    
    print(':: TIMEOUT    : %i' % timeout)
    print(':: USER-AGENT : %s' % user_agent)
    
    if verify:
        print(':: VERIFY     : True')
    else:
        print(':: VERIFY     : False')
    print('')

def show_payloads_log():
    print('')
    print(f'[\033[4m{green}INJECTION\033[0m]')
    print('|-','Set-Cookie:param=crlfsuite;')
    print('\n'+f'[\033[4m{green}XSS PAYLOADS (for CRLF injection)\033[0m]')
    for p in xss_payloads:
        print('|-', p)
    print('\n'+f'[\033[4m{green}APPEND STRINGS\033[0m]')
    for appstr in starting_strings:
        print('|-',appstr)
    print('\n'+f'[\033[4m{green}ESCAPE CHARS\033[0m]')
    for char in escape_chars:
        print('|-',char)
