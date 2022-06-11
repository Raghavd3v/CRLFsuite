# -*- coding: utf-8 -*-

import sys
from crlfsuite.core.cli import url, threads, urls, silent, method, std, cookies, data, user_agent, timeout, verify, read_urls, output_file, s_payloads
from crlfsuite.core.crlfscanner import crlfscanner
from concurrent.futures import ThreadPoolExecutor, as_completed
from crlfsuite.utils.utils import build_url
from crlfsuite.core import logger
from crlfsuite.core.logger import args_info, green, reset, bright, red, show_payloads_log
from crlfsuite.core.config import vuln_urls
from datetime import datetime
from crlfsuite.plugins.wafdetector import WafDetector

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M")

if not silent:
    args_info(url, urls, std, output_file, method, data, cookies, timeout, user_agent["User-Agent"], verify, threads)
    logger.info('CRLFsuite v2.0 (%sCRLF vulnerability Scanner%s)' % (green,reset))
    logger.warn('Use with caution. You are responsible for your actions')
    logger.warn('Developers assume no liability and are not responsible for any misuse or damage.')

if s_payloads:
    show_payloads_log()
    quit()

if urls:
    total_parsed_urls = []
    for each_url in read_urls:
        parsed_urls = build_url(each_url)
        for each_parsed_url in parsed_urls[0]:
            total_parsed_urls.append(each_parsed_url)

if std:
    stdin_urls = []
    stdin_data = sys.stdin.readlines()
    for each_url in stdin_data:
        parse_urls = build_url(each_url.strip())
        for each_parsed_url in parse_urls[0]:
            stdin_urls.append(each_parsed_url)
if url:
    Wafstatus = WafDetector(url)
    if Wafstatus:
        logger.info('WAF status: %sonline%s' %(green,reset))
        logger.warn(Wafstatus+' - %s%sWAF detected!%s' % (bright,red, reset))
    else:
        logger.info('WAF status: %soffline%s' % (green,reset))
else:
    logger.info('WAF Detector only works with single URL scanning')

def main():
    if url:
        parsed_urls = build_url(url)
        logger.info('Initiating Heuristic Scannner at %s ...\n' % dt_string)
        with ThreadPoolExecutor(max_workers=threads) as executor:
            tasks = []
            for u in parsed_urls[0]:
                task = executor.submit(crlfscanner, u, method, cookies, data, user_agent, timeout, verify, output_file)
                tasks.append(task)
            for i, _ in enumerate(as_completed(tasks)):
                print('%s[%s*%s%s]%s Progress: %i/%i' % (bright,green,reset,bright,reset,i+1, parsed_urls[1]), end='\r')
        if len(vuln_urls) == 0:
            logger.bad("No CRLF injection detected")
        else:
            for URL in vuln_urls:
                logger.good(URL)
    elif urls:
        logger.info('Initiating Heuristic Scanner at %s ...\n' % dt_string)
        with ThreadPoolExecutor(max_workers=threads) as executor:
            tasks = []
            for u in total_parsed_urls:
                task = executor.submit(crlfscanner, u, method, cookies, data, user_agent, timeout, verify, output_file)
                tasks.append(task)
            for i, _ in enumerate(as_completed(tasks)):
                print('%s[%s*%s%s]%s Progress: %i/%i' % (bright,green,reset,bright,reset,i+1, len(total_parsed_urls)), end='\r')
        if len(vuln_urls) == 0:
            logger.bad("No CRLF injection detected")
        else:
            for URL in vuln_urls:
                logger.good(URL)
    elif std:
        logger.info('Initiating Heuristic Scanner at %s ...\n' % dt_string)
        with ThreadPoolExecutor(max_workers=threads) as executor:
            tasks = []
            for u in stdin_urls:
                task = executor.submit(crlfscanner, u, method, cookies, data, user_agent, timeout, verify, output_file)
                tasks.append(task)
            for i, _ in enumerate(as_completed(tasks)):
                print('%s[%s*%s%s]%s Progress: %i/%i' % (bright,green,reset,bright,reset,i+1, len(stdin_urls)), end='\r')
        if len(vuln_urls) == 0:
            logger.bad("No CRLF injection detected")
        else:
            for URL in vuln_urls:
                logger.good(URL)
    else:
        logger.error('URL(s) not specified!')
        logger.info('Try using -u/-i/-s options')
        quit()
