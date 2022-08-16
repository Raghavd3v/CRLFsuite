# -*- coding: utf-8 -*-

import re

def inject(url,payload):
    """
    Injects the payload in the parameters and returns a set
    """
    injected_url = set()
    temp_payload = payload.replace('\\n', '$').replace('\\t', '@').replace('\\r', '!') #saves the payload from the removal of \\n, \\t and \\r
    injected = re.sub(r"=[^?\|&]*", '=' + str(temp_payload), str(url))
    final_payload = injected.replace('$', '\\n').replace('@', '\\t').replace('!', '\\r')
    injected_url.add(final_payload)
    
    return injected_url