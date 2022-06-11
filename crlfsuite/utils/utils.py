# -*- coding: utf-8 -*-

import random
from urllib.parse import parse_qs
from http.cookies import SimpleCookie
from crlfsuite.core.config import xss_payloads

def parse_post_data(data):
    result = parse_qs(data, strict_parsing=True)
    for key in result:
        if len(result[key]) == 1:
            result[key] = result[key][0]
            data = result
    
    return data

def parse_cookies(cookies):
    raw_data = cookies
    cookie = SimpleCookie()
    cookie.load(raw_data)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    
    return cookies

def get_user_agent():
    #Thanks @devanshbatham for this list.
    user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    ]

    user_agent_header = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent_header}

    return headers

def build_url(url):
    parsed_urls = set()
    starting_strings = ["", "crlfsuite", "?crlfsuite=", "#", '__session_start__/']
    escape_chars = ['%0d','%0a', '%0d%20', '%0a%20' , '%3f' , '%0d%0a', '%23%0d', '%23%0a', '%23%0d%0a', '%u000a', '%25%30%61', '%25%30a', '%3f%0d', '%3f%0d%0a', '%3f%0a' , '%%0a0a', '%u000d', '%u0000', '%0d%09', '%0d%0a%09', '%0d%0a%20' , '%25250a', '%250a', '%2F..%0d%0a', '%2f%2e%2e%0d%0a', '%25%30' , '%2e%2e%2f%0d%0a', '%E5%98%8A%E5%98%8D%E5%98%8A%E5%98%8D', '%E5%98%8A%E5%98%8D', '%e5%98%8a%e5%98%8d%0a', '%e5%98%8a%e5%98%8d%0d', '%e5%98%8a%e5%98%8d%0d%0a' , f"\\r", f"\\r\\n", f"\\r\\t", f"\\r\\n\\t", f"\\r%20", f"\\r\\n%20"]
    injection = "Set-Cookie:param=crlfsuite;"

    if not url.endswith('/'):
        url = url+'/'
    else:
        pass
    
    for string in starting_strings:
        for each_escape in escape_chars:
            parsed_urls.add(url+string+each_escape+injection)
    
    for payload in xss_payloads:
        if url.endswith('/'):
            newurl = (url+payload)
        else:
            newurl = (url+'/'+payload)
        
        parsed_urls.add(newurl)
    
    total_len = len(parsed_urls)
    
    return parsed_urls, total_len