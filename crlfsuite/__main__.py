# -*- coding: utf-8 -*-

import warnings
from sys import stdin
from datetime import datetime
from crlfsuite.core import logger
from crlfsuite.core.generator import generate
from crlfsuite.plugins.heuristic import heuristic_scanner
from crlfsuite.plugins.wafDetector import WafDetector
from crlfsuite.utils import cleaner
from crlfsuite.utils.parser import parse_cookies, parse_post_data, extract_headers
from crlfsuite.utils.randomagents import get_user_agent
from crlfsuite.core.resumer import resume as resumer, extract_index
from crlfsuite.core.prompt import prompt
from crlfsuite.utils.temp import create_temp_file
from crlfsuite.utils.reader import reader
from crlfsuite.core.logger import args_info, green, reset, bright, progress, banner
from concurrent.futures import ThreadPoolExecutor, as_completed
from crlfsuite.core.scanner import scanner
from crlfsuite.core.exporter import exporter
from crlfsuite.core.resumer import create_resume_file
from crlfsuite.utils.percentage import get_percentage
from crlfsuite.core.config import vuln_urls, heuristic_result, heuristic_payload
from crlfsuite.core.cli import target, targets, timeout, pipe, method, data, headers, ssl, jout, \
nout, threads, verbose, silent, skipHeuristic, cookie, clean as cl, stable, delay, resume

warnings.filterwarnings('ignore')

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y %H:%M")

if not silent:
    print(banner)
    args_info(target, targets, pipe, nout, jout, method, data, cookie, timeout, ssl, threads, verbose, delay)
    logger.info('CRLFsuite v2.5.2 (%sCRLF Injection Scanner%s)' % (green,reset))
    logger.warn('Use with caution. You are responsible for your actions')
    logger.warn('Developers assume no liability and are not responsible for any misuse or damage.')
else:
    None

if cookie:
    if not silent:
        if verbose >= 1:
            logger.info('Parsing cookies')
    cookie = parse_cookies(cookie)
    if not silent:
        if verbose >= 3:
            logger.info('Parsed cookies: {}'.format(cookie))
else:
    None

if data:
    if not silent:
        if verbose >= 1:
            logger.info('Parsing HTTP POST data')
    data = parse_post_data(data)
    if not silent:
        if verbose >= 3:
            logger.info('Parsed POST data: {}'.format(data))
else:
    None

if headers:
    if not silent:
        if verbose >= 1:
            logger.info('Parsing and extracting headers')
    if type(headers) == str:
        headers = extract_headers(headers)
    else:
        headers = extract_headers(prompt())
    if not silent:
        if verbose >= 3:
            logger.info('Parsed headers: {}'.format(headers))
else:
    if not silent:
        if verbose >= 1:
            logger.info('Generating random headers')
    headers = get_user_agent()

if stable or delay:
    if not silent:
        if verbose >= 1:
            logger.info('Setting threads to 1')
    threads = 1

if resume:
    if not silent:
        if verbose >= 1:
            logger.info('Extracting index from resume.cfg and resuming the scan')
    try:
        index = extract_index(silent)
        if index:
            resumer(index, threads, method, cookie, timeout, data, ssl, headers, nout, jout, verbose, silent, stable, delay)
            quit()
    except Exception as e:
        if not silent:
            logger.error(e)

if target:
    if not skipHeuristic:
        if not silent:    
            if verbose >= 1:
                logger.info('Intializing Heuristic scanner...')
        heuristic_scanner(target, heuristic_payload, method, cookie, headers, timeout, ssl, data, verbose, silent, stable, delay)
        if not silent:
            if verbose >= 1:
                logger.info('Heuristic scan completed.')
    if not silent: #Running WafDetector in silent mode is useless
        if verbose >= 1:
            logger.info('Intializing WAF detector at %s...' % dt_string)
        Wafstatus = WafDetector(target)
        if Wafstatus:
            logger.info('WAF status: %sonline%s' %(green,reset))
            if verbose >= 2:
                logger.info('WAF detected: %s' % Wafstatus)
        else:
            logger.info('WAF status: %soffline%s' % (green,reset))
        if verbose >= 1:
            logger.info('WAF detection completed.')
    total_parsed_targets = []
    if not silent:
        if verbose >= 1:
            logger.info('Intializing Payload Generator...')
    parsed_target = generate(target)
    for each in parsed_target[0]:
        total_parsed_targets.append(each)
    if not silent:
        if verbose >= 2:
            logger.info('Total URL(s) generated: {}'.format(len(total_parsed_targets)))
elif targets:
    total_parsed_targets = []
    read_urls = reader(targets)
    if not skipHeuristic:
        if not silent:    
            if verbose >= 1:
                logger.info('Intializing Heuristic scanner...')
        for each_url in read_urls:
            heuristic_scanner(each_url, heuristic_payload, method, cookie, headers, timeout, ssl, data, verbose, silent, stable, delay)
        if not silent:
            if verbose >= 1:
                logger.info('Heuristic scan completed.')
    if not silent:
        if verbose >= 1:
            logger.info('Intializing Payload Generator...')
    for _each_url in read_urls:
        parsed_targets = generate(_each_url)
        for each in parsed_targets[0]:
            total_parsed_targets.append(each)
    if not silent:
        if verbose >= 2:
            logger.info('Total URL(s) generated: {}'.format(len(total_parsed_targets)))
elif pipe:
    total_parsed_targets = []
    pipe_data = stdin.read().splitlines()
    if not skipHeuristic:
        if not silent:
            if verbose >= 1:
                logger.info('Intializing Heuristic scanner...')
        for each_std_url in pipe_data:
            heuristic_scanner(each_std_url, heuristic_payload, method, cookie, headers, timeout, ssl, data, verbose, silent, stable, delay)
        if not silent:
            if verbose >= 1:
                logger.info('Heuristic scan completed.')
    if not silent:
        if verbose >= 1:
            logger.info('Intializing Payload Generator...')
    for std_url in pipe_data:
        parsed_std_urls = generate(std_url)
        for each in parsed_std_urls[0]:
            total_parsed_targets.append(each)
    if not silent:
        if verbose >= 2:
            logger.info('Total URL(s) generated: {}'.format(len(total_parsed_targets)))
else:
    if not silent:
        logger.error('Target(s) not specified.')
    quit()

if not silent:
    if not skipHeuristic:
        if not len(heuristic_result) == 0:
            logger.good('Heuristic test shows that %s%s%s is/are might be injectable' % (bright,', '.join([str(each_u) for each_u in heuristic_result]), reset))
        else:
            logger.info('Heuristic scanner found no injectable URL(s).')

if not silent:
    logger.info('Creating resumable_data.crlfsuite.')
create_temp_file(total_parsed_targets)

def main():
    if target:
        try:
            if not silent:
                if verbose >= 1:
                    logger.info('Intializing CRLF Injection scanner at %s...' % dt_string )
            with ThreadPoolExecutor(max_workers=threads) as executor:
                tasks = []
                for u in total_parsed_targets:
                    task = executor.submit(scanner, u.strip(), method, cookie, timeout, data, ssl, headers, verbose, silent, stable, delay)
                    tasks.append(task)
                for i, _ in enumerate(as_completed(tasks)):
                    if not silent:
                        print(progress+'Progress: %i/%i (%i%%)' % (i+1, len(total_parsed_targets), get_percentage(i+1, len(total_parsed_targets))), end='\r')
        except KeyboardInterrupt as k:
            if not silent:
                logger.error('Interrupt detected. Creating %sresume.cfg%s.' % (bright,reset))
            create_resume_file(i)
            quit(k)
    elif targets:
        try:
            if not silent:
                if verbose >= 1:
                    logger.info('Intializing CRLF Injection scanner at %s...' % dt_string)
            with ThreadPoolExecutor(max_workers=threads) as executor:
                tasks = []
                for u in total_parsed_targets:
                    task = executor.submit(scanner, u.strip(), method, cookie, timeout, data, ssl, headers, verbose, silent, stable, delay)
                    tasks.append(task)
                for i, _ in enumerate(as_completed(tasks)):
                    if not silent:
                       print(progress+'Progress: %i/%i (%i%%)' % (i+1, len(total_parsed_targets) ,get_percentage(i+1, len(total_parsed_targets))), end='\r') 
        except KeyboardInterrupt as k:
            if not silent:
                logger.error('Interrupt detected. Creating %sresume.cfg%s.' % (bright,reset))
            create_resume_file(i)
            quit(k)
    elif pipe:
        try:
            if not silent:
                if verbose >= 1:
                    logger.info('Intializing CRLF Injection scanner at %s...' % dt_string)
            with ThreadPoolExecutor(max_workers=threads) as executor:
                tasks = []
                for u in total_parsed_targets:
                    task = executor.submit(scanner, u.strip(), method, cookie, timeout, data, ssl, headers, verbose, silent, stable, delay)
                    tasks.append(task)
                for i, _ in enumerate(as_completed(tasks)):
                    if not silent:
                       print(progress+'Progress: %i/%i (%i%%)' % (i+1, len(total_parsed_targets), get_percentage(i+1, len(total_parsed_targets))), end='\r') 
        except KeyboardInterrupt as k:
            if not silent:
                logger.error('Interrupt detected. Creating %sresume.cfg%s.' % (bright,reset))
            create_resume_file(i)
            quit(k)  
    else:
        None
    
    if not len(vuln_urls) == 0 or len(heuristic_result) == 0:
        total_vuln_urls = vuln_urls.union(heuristic_result)
        if not silent:
            print('%-60s' % '') #cleans the progress
            for vuln_url in total_vuln_urls:
                logger.good(vuln_url)
        if nout or jout:
            if not silent:
                if verbose >= 1:
                    logger.info('Writing output')
        exporter(nout, jout, total_vuln_urls)
    else:
        logger.bad('No CRLF Injection found.')

    if cl:
        if not silent:
            if verbose >= 1:
                logger.info('Removing CRLFsuite generated files.')
        cleaner.clean()
    else:
        None

if __name__ == '__main__':
    main()