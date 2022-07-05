# -*- coding: utf-8 -*-
import requests
import warnings
from crlfsuite.core.cli import verbose
from crlfsuite.core.config import vuln_urls
from crlfsuite.core import logger
warnings.filterwarnings('ignore')

def crlfscanner(url, method, cookies, data, user_agent, timeout, verify, output):
    if verbose:
        logger.verbosity('Testing: %s' % url)
    try:
        if method == "POST":
            try:
                req = requests.post(url.strip(), data=data, cookies=cookies, headers=user_agent, timeout=timeout, verify=verify, allow_redirects=False)
            except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.SSLError, requests.exceptions.HTTPError, requests.exceptions.InvalidURL):
                if verbose:
                    logger.error('Error while sending request: %s' % url)
            #if 'param' in str(req.cookies.get_dict()) and 'crlfsuite' in str(req.cookies.get_dict().values()):
            code = req.text
            content = req.text
            
            try:
                headers = req.headers["Set-Cookie"]
            except KeyError:
                None
            
            if not code >= 400:
                if 'param' in headers:
                    if 'crlfsuite' in headers:    
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
            
            try:
                if not code >= 400:
                    #if 'svg/onload=alert(innerHTML()' in content or '<svg onload=alert(document.domain)>' in content or '<script>alert(\"XSS\")</script>' in content or 'Injected' in content or '<script>alert(document.domain)</script>' in content or '<script>alert(document.cookie)</script>' in content:
                    if "svg/onload=alert(innerHTML()" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<svg onload=alert(document.domain)>" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<script>alert(\"XSS\")</script>" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "Injected" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<script>alert(document.domain)</script>" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<script>alert(document.cookie)</script>" in content:
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
        else:
            try:
                req = requests.get(url.strip(), cookies=cookies, headers=user_agent, timeout=timeout, verify=verify, allow_redirects=False)
            except (requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.SSLError, requests.exceptions.HTTPError, requests.exceptions.InvalidURL):
                if verbose:
                    logger.error('Error while sending request: %s' % url)
            #if 'param' in str(req.cookies.get_dict()) and 'crlfsuite' in str(req.cookies.get_dict().values()):
            code = req.status_code
            content = req.text
            
            try:
                headers = req.headers["Set-Cookie"]
            except KeyError:
                None
            
            if not code >= 400:
                if 'param' in headers:
                    if 'crlfsuite' in headers:
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
            
            try:
                if not code >= 400:
                    #if 'svg/onload=alert(innerHTML()' in content or '<svg onload=alert(document.domain)>' in content or '<script>alert(\"XSS\")</script>' in content or 'Injected' in content or '<script>alert(document.domain)</script>' in content or '<script>alert(document.cookie)</script>' in content:
                    if "svg/onload=alert(innerHTML()" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<svg onload=alert(document.domain)>" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<script>alert(\"XSS\")</script>" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "Injected" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<script>alert(document.domain)</script>" in content:
                        vuln_urls.append(url)
                        if output:
                            with open(output, 'a') as file:
                                file.write(url.strip())
                                file.write('\n')
                            file.close()
                    elif "<script>alert(document.cookie)</script>" in content:
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
    except KeyboardInterrupt:
        pass