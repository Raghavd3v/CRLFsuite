# -*- coding: utf-8 -*-

import re
import requests
import warnings
from crlfsuite.core.config import vuln_urls

warnings.filterwarnings('ignore')

def crlfscanner(url, method, cookies, data, user_agent, timeout, verify, output):
    try:
        if method == "POST":
            req = requests.post(url.strip(), data=data, cookies=cookies, headers=user_agent, timeout=timeout, verify=verify)
            #if 'param' in str(req.cookies.get_dict()) and 'crlfsuite' in str(req.cookies.get_dict().values()):
            code = req.text
            content = req.text
            keys = str(req.cookies.get_dict().keys())
            values = str(req.cookies.get_dict().values())
            
            if code >= 400:
                if re.search('param', keys, re.I):
                    if re.search('crlfsuite', values, re.I):    
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                        else:
                            None
                    else:
                        None
                else:
                    None
            
            if not code >= 400:
                if 'svg/onload=alert(innerHTML()' in content or '<svg onload=alert(document.domain)>' in content or '<script>alert(\"XSS\")</script>' in content or 'Injected' in content or '<script>alert(document.domain)</script>' in content or '<script>alert(document.cookie)</script>' in content:
                    vuln_urls.append(url)
                    if output:
                        with open(output, 'a') as file:
                            file.write(url)
                            file.write('\n')
                        file.close()
                else:
                    None
            else:
                None
        else:
            req = requests.get(url.strip(), cookies=cookies, headers=user_agent, timeout=timeout, verify=verify)
            #if 'param' in str(req.cookies.get_dict()) and 'crlfsuite' in str(req.cookies.get_dict().values()):
            code = req.status_code
            content = req.text
            keys = str(req.cookies.get_dict().keys())
            values = str(req.cookies.get_dict().values())
            
            if code >= 400:
                if re.search('param', keys, re.I):
                    if re.search('crlfsuite', values, re.I):
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                        else:
                            None
                    else:
                        None
                else:
                    None
            
            if not code >= 400:
                if 'svg/onload=alert(innerHTML()' in content or '<svg onload=alert(document.domain)>' in content or '<script>alert(\"XSS\")</script>' in content or 'Injected' in content or '<script>alert(document.domain)</script>' in content or '<script>alert(document.cookie)</script>' in content:
                    vuln_urls.append(url)
                    if output:
                        with open(output, 'a') as file:
                            file.write(url.strip())
                            file.write('\n')
                        file.close()
                else:
                    None
            else:
                None

    except Exception:
        pass