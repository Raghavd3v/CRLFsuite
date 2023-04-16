# -*- coding: utf-8 -*-

import re
from crlfsuite.core import requester
from crlfsuite.core.config import vuln_urls

def scanner(url, method, cookie, timeout, data, ssl, headers, verbose, silent, stable, delay):
    """
    Checks if the URL is vulnerable or not
    """
    response = requester.do(url, 
                        method, 
                        cookie, 
                        headers, 
                        timeout, 
                        ssl, 
                        data,
                        verbose,
                        silent,
                        stable,
                        delay,
                )
    try:
        text ,status_code, rheaders = response[0], response[1], response[2]
    except TypeError:
        pass
    if not int(status_code) >= 400:
        if 'nefcore' in rheaders or 'crlfsuite' in rheaders:
            vuln_urls.add(url)
        if "svg/onload=alert(innerHTML()" in text:
            vuln_urls.add(url)
        if "<svg onload=alert(document.domain)>" in text:
            vuln_urls.add(url)
        if "<script>alert(\"XSS\")</script>" in text:
            vuln_urls.add(url)
        if "<html>Injected Content<html>" in text:
            vuln_urls.add(url)
        if "<script>alert(document.domain)</script>" in text:
            vuln_urls.add(url)
        if "<script>alert(document.cookie)</script>" in text:
            vuln_urls.add(url)