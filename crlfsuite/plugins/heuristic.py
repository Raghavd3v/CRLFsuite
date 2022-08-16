# -*- coding: utf-8 -*-

from urllib.parse import urlparse
from crlfsuite.core import requester
from crlfsuite.core.config import heuristic_result

def heuristic_scanner(url, payload, method, cookie, headers, timeout, ssl, data, verbose, silent, stable, delay):
    """
    A basic scan to check if the URL is vulnerable or not
    """
    url = url.strip()
    scheme, host = urlparse(url).scheme, urlparse(url).netloc
    url = (scheme+'://'+host)
    if not url.endswith('/'):
        url = url+'/'
    final_url = (url+payload)
    response = requester.do(final_url, method, cookie, headers, timeout, ssl, 
                        data,
                        verbose,
                        silent,
                        stable,
                        delay
                )
    try:
        code, rheaders = response[1], str(response[2])
        if not int(code) >= 400:
            if 'nefcore' and 'crlfsuite' in rheaders:
                heuristic_result.add(final_url)
    except TypeError:
        pass