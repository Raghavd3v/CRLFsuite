# -*- coding: utf-8 -*-

from urllib.parse import parse_qs
from http.cookies import SimpleCookie

def parse_post_data(data):
    """
    parses the post data
    """
    result = parse_qs(data, strict_parsing=True)
    for key in result:
        if len(result[key]) == 1:
            result[key] = result[key][0]
            data = result
    
    return data

def parse_cookies(cookies):
    """
    converts the raw data to dict
    """
    raw_data = cookies
    cookie = SimpleCookie()
    cookie.load(raw_data)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    
    return cookies

def extract_headers(headers):
    """
    extracts the headers and returns a dict
    """
    headers = headers.replace('\\n', '\n')
    return parse_headers(headers)

def parse_headers(string):
    """
    parses the headers and creates a dict
    """
    new_headers = {}
    for line in string.split('\n'):
        if len(line) > 1:
            splitted = line.split(':')
            new_headers[splitted[0]] = ':'.join(splitted[1:]).strip()

    return new_headers
