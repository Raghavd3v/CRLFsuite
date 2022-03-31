# -*- coding: utf-8 -*-

import requests
import warnings
from crlfsuite.core.config import vuln_urls
from crlfsuite.core.cli import output_file

warnings.filterwarnings('ignore')

def crlfscanner(url, method, cookies, data, user_agent, timeout, verify):
    try:
        if method == "POST":
            req = requests.post(url.strip(), data=data, cookies=cookies, headers=user_agent, timeout=timeout, verify=verify)
            if 'param' in req.cookies.get_dict() and 'crlfsuite' in req.cookies.get_dict().values():
                vuln_urls.append(url)
                with open(output_file, 'a') as output:
                    output.write(url.strip())
                    output.write('\n')
                output.close()
            else:
                pass
        else:
            req = requests.get(url.strip(), cookies=cookies, headers=user_agent, timeout=timeout, verify=verify)
            if 'param' in req.cookies.get_dict() and 'crlfsuite' in req.cookies.get_dict().values():
                vuln_urls.append(url)
                with open(output_file, 'a') as output:
                    output.write(url.strip())
                    output.write('\n')
                output.close()
            else:
                pass
    except Exception:
        pass