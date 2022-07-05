# -*- coding: utf-8 -*-

import argparse
from crlfsuite.utils.utils import get_user_agent, parse_cookies, parse_post_data
from crlfsuite.core.logger import banner
from crlfsuite.core import logger

parser = argparse.ArgumentParser()
required_grp = parser.add_argument_group('Main options') 
required_grp.add_argument('-u', '--url', dest='url', help='Specify the target URL (Example: -u https://google.com)')
required_grp.add_argument('-i', '--import-urls', help='Import targets from the file (Example: -i targets.txt)')
required_grp.add_argument('-s', '--stdin', help='Scan URLs from stdin', action="store_true")
required_grp.add_argument('-o', '--output', help='Path for output file (Example: /home/devansh/output.txt)')
request_grp = parser.add_argument_group('Request options')
request_grp.add_argument('-m','--method', dest='method', help='Request method (GET/POST), Default is GET', default="GET")
request_grp.add_argument('-d','--data', dest='data', help='POST data (Example: --data "squery=google&data=hacked")')
request_grp.add_argument('-uA','--user-agent', help='Specify User-Agent (Example: Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0)', default=get_user_agent())
request_grp.add_argument('-To','--timeout', help='Connection timeout, default is 15', default=15)
request_grp.add_argument('-c','--cookies', help='Specify cookies if required (Example: --cookies "PASS=TEST; hack=hack")')
request_grp.add_argument('-v','--verify', help='Verify SSL cert, Default is false', default=False, action='store_true')
request_grp.add_argument('-verbose', help='Verbosity', action='store_true')
other_grp = parser.add_argument_group('Other options')
other_grp.add_argument('-t', '--threads', dest='threads', help='Number of concurrent threads, default is 50.',default=50, type=int)
other_grp.add_argument('-sB', '--skip-banner', help='Skip banner and args info (direct output)', action="store_true")
other_grp.add_argument('-sP', '--show-payloads', help='Show all the available CRLF payloads', action='store_true')

args = parser.parse_args()
url = args.url
urls = args.import_urls
method = args.method
verbose = args.verbose
data = args.data
user_agent = args.user_agent
timeout = args.timeout
cookies = args.cookies
s_payloads = args.show_payloads
output_file = args.output
verify = args.verify
threads = args.threads
std = args.stdin
silent = args.skip_banner

if not silent:
    print(banner)
    
read_urls = ""

if urls:
    if verbose:
        logger.verbosity('Loading URLs...')
    with open(urls, 'r') as targets:
        read_urls = targets.read().splitlines()
else:
    pass

if data:
    if verbose:
        logger.verbosity('Parsing POST data...')
    new_data = parse_post_data(data)
else:
    pass

if cookies:
    if verbose:
        logger.verbosity('Parsing cookies...')
    new_cookies = parse_cookies(cookies)
else:
    pass
