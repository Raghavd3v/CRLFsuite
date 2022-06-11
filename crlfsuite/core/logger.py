# -*- coding: utf-8 -*-

from colorama import Fore as clr, Style
from crlfsuite.core.config import escape_chars, starting_strings
cyan = clr.CYAN
green = clr.LIGHTGREEN_EX
yellow = clr.LIGHTYELLOW_EX
red = clr.RED
bright = Style.BRIGHT
blue = clr.BLUE 
reset = Style.RESET_ALL

banner = f"""                       
 ______     ______     __         ______   ______     __  __     __     ______   ______    
/\  ___\   /\  == \   /\ \       /\  ___\ /\  ___\   /\ \/\ \   /\ \   /\__  _\ /\  ___\   
\ \ \____  \ \  __<   \ \ \____  \ \  __\ \ \___  \  \ \ \_\ \  \ \ \  \/_/\ \/ \ \  __\   
 \ \_____\  \ \_\ \_\  \ \_____\  \ \_\    \/\_____\  \ \_____\  \ \_\    \ \_\  \ \_____\ 
  \/_____/   \/_/ /_/   \/_____/   \/_/     \/_____/   \/_____/   \/_/     \/_/   \/_____/ v2.0
                                                                                        
                                                ({green}\x1B[3mBy Nefcore Security\x1B[0m{reset})
"""

def good(msg):
    print("[" + green + bright +'VLN' + reset + '] '+msg)

def bad(msg):
    print("[" + clr.LIGHTMAGENTA_EX + bright + 'NOT VLN' + reset + '] '+msg)

def error(msg):
    print("[" + red + bright +'ERR' + reset + ']',msg)

def info(msg):
    print("[" + blue + 'INF' + reset + "] "+msg)

def warn(msg):
    print("[" + yellow + 'WRN' + reset + "] "+msg)

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
    print('INJECTION')
    print('========='+'\n')
    print(f'{bright}[{green}+{reset}{bright}]{reset}','Set-Cookie:param=crlfsuite;')
    print('\n'+'APPEND STRINGS')
    print('=============='+'\n')
    for appstr in starting_strings:
        print(f'{bright}[{green}+{reset}{bright}]{reset}',appstr)
    print('\n'+'ESCAPE CHARS')
    print('============'+'\n')
    for char in escape_chars:
        print(f'{bright}[{green}+{reset}{bright}]{reset}',char)
