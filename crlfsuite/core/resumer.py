# -*- coding: utf-8 -*-

import os
from crlfsuite.utils.reader import reader
from concurrent.futures import ThreadPoolExecutor, as_completed
from crlfsuite.core.scanner import scanner
from crlfsuite.core import logger
from crlfsuite.core.logger import banner, progress
from crlfsuite.utils.percentage import get_percentage
from crlfsuite.core.config import vuln_urls
from crlfsuite.utils import cleaner
from crlfsuite.core.exporter import exporter

def create_resume_file(i):
    """
    writes the index in the resume.cfg file
    """
    with open('resume.cfg', 'w+', encoding='utf-8') as resume_file:
        resume_file.write('index=%i' % i)

def extract_index(silent):
    """
    extracts the index from resume.cfg file
    """
    if os.path.isfile('resume.cfg'):
        read = reader('resume.cfg')
    else:
        if not silent:
            logger.error('resume.cfg not found')
        quit()
    for x in read:
        splitit = x.split('=')
        index = splitit[1]

    return index

def resume(i, threads, method, cookie, timeout, data, ssl, headers, nout, jout, verbose, silent, stable, delay):
    """
    resumes the scan from the extracted index 
    """
    try:
        if not silent:
            print(banner)
        if os.path.isfile('resumable_data.crlfsuite'):
            read = reader('resumable_data.crlfsuite')
        else:
            if not silent:
                logger.error('resumable_data.crlfsuite not found')
            quit()
        if not silent:
            if verbose >= 1:
                logger.info('Resuming...')
        with ThreadPoolExecutor(max_workers=threads) as executor:
            index = (int(i)-1)
            tasks = []
            for url in read[int(index):]:
                task = executor.submit(scanner, url.strip(), method, cookie, timeout, data, ssl, headers, verbose, silent, stable, delay)
                tasks.append(task)
            for done, _ in enumerate(as_completed(tasks)):
                if not silent:
                    print(progress+'Progress: %i/%i (%i%%)' % (done+1, len(read[int(index):]), get_percentage(done+1, len(read[int(index):]))), end='\r')
        if not len(vuln_urls) == 0: 
            print('%-60s' % '')
            if not silent:
                for vuln_url in vuln_urls:
                    logger.good(vuln_url)
            exporter(nout, jout, vuln_urls)
        else:
            logger.bad('No CRLF Injection found.')
        cleaner.clean()
    except Exception as e:
        print(e)