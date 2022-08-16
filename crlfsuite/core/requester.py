# -*- coding: utf-8 -*-

import requests
import warnings
import random
from crlfsuite.core import logger
from time import sleep
from crlfsuite.core.logger import reset, bright

warnings.filterwarnings('ignore')

def do(url, method, cookie, headers, timeout, ssl, data, verbose, silent, stable, delay):
    """
    Sends HTTP requests and retuns text, headers and status code of the response
    """
    if stable:
        delay = random.choice(range(5, 15))
    sleep(delay)
    try:
        if method == "GET":
            request = requests.get(url, 
                            cookies=cookie, 
                            headers=headers, 
                            timeout=timeout, 
                            verify=ssl,
                            )
            response = request.text
            status_code = request.status_code
            response_headers = request.headers
            if verbose >= 2:
                logger.info('GET Request: %s' % url)
                logger.info(f'  - Status Code: {status_code}')
            if verbose >= 3:
                logger.info(f'  - Response headers: {response_headers}')
                logger.info(f'  - Response text: {response}')
        elif method == "POST":
            request = requests.post(url,
                            data=data,
                            cookies=cookie,
                            headers=headers,
                            timeout=timeout,
                            verify=ssl,
                            )
            response = request.text
            status_code = request.status_code
            response_headers = request.headers
            if verbose >= 2:
                logger.info('POST Request: %s' % url)
                logger.info(f'  - Status Code: {status_code}')
            if verbose >= 3:
                logger.info(f'  - Response headers: {response_headers}')
                logger.info(f'  - Response text: {response}')
        return response, status_code, response_headers
    except requests.exceptions.ConnectionError:
        if not silent:
            if verbose >= 2:
                logger.error('Can\'t connect to the server: %s' % url)
    except requests.exceptions.HTTPError as e:
        if not silent:
            if verbose >= 2:
                logger.error('%s: %s' % (e,url))
    except requests.exceptions.Timeout:
        if not silent:
            if verbose >= 2:
                logger.error('Timeout Error: %s' % url)
    except requests.exceptions.RequestException as e:
        if not silent:
            if verbose >= 2:
                logger.error('%s: %s' % (e, url))
