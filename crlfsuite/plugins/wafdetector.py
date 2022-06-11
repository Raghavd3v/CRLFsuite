#s0md3v :) - Just using your methodology

import re
import json
import requests

crlfsuite_dir = __file__.replace('/plugins/wafdetector.py', '')

def WafDetector(url):
    with open(crlfsuite_dir+'/db/wafsign.json', 'r') as file:
        wafsigns = json.load(file)
    payload = "../../../etc/passwd"
    response = requests.get(url+'/'+payload)
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
                    total_score += 0.5 #not a strong indicator
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