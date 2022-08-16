# -*- coding: utf-8 -*-

import re
import json
import requests
import warnings
from urllib.parse import urlparse
from crlfsuite.utils.compatible import compatible_path
warnings.filterwarnings('ignore')

crlfsuite_dir = compatible_path(__file__.replace(compatible_path('/crlfsuite/plugins/wafDetector.py'), ''))

def WafDetector(url):
    """
    Checks if the WAF is online or offline using wafsignatures.json
    """
    try:
        domain, scheme, path = urlparse(url).netloc, urlparse(url).scheme, urlparse(url).path
        url = (scheme+'://'+domain+path)
        if not url.endswith('/'):
            url = url+'/'
        signature_file = crlfsuite_dir+'/crlfsuite/db/wafsignatures.json'
        signature_file = compatible_path(signature_file)
        with open(signature_file, 'r', encoding='utf-8') as file:
            wafsigns = json.load(file)
        payload = "../../../etc/passwd"
        response = requests.get(url+payload)
        code = str(response.status_code)
        page = response.text
        headers = str(response.headers)
        cookie = str(response.cookies.get_dict())
        if int(code) >= 400:
            bmatch = [0, None]
            for wafname, wafsign in wafsigns.items():
                total_score = 0
                pSign = wafsign["page"]
                cSign = wafsign["code"]
                hSign = wafsign["headers"]
                ckSign = wafsign["cookie"]
                if pSign:
                    if re.search(pSign, page, re.I):
                        total_score += 1
                if cSign:
                    if re.search(cSign, code, re.I):
                        total_score += 0.5
                if hSign:
                    if re.search(hSign, headers, re.I):
                        total_score += 1
                if ckSign:
                    if re.search(ckSign, cookie, re.I):
                        total_score += 1
                if total_score > bmatch[0]:
                    del bmatch[:]
                    bmatch.extend([total_score, wafname])
            if bmatch[0] != 0:
                return bmatch[1]
            else:
                None
        else:
            None
    except Exception as e:
        pass