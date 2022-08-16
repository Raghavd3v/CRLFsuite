# -*- coding: utf-8 -*-

import json

def normal_output(nout, urls):
    """
    exports vulnerable URL(s) to a text file
    """
    with open(nout, 'w+', encoding='utf-8') as file:
        for url in urls:
            file.write(url)
            file.write('\n')

def json_output(jout, urls):
    """
    exports vulnerable URL(s) in json format
    """
    result = {}
    for url in urls:
        result[url] = {}
        result[url]['Vulnerable'] = True
    with open(jout, 'w+', encoding='utf-8') as json_out:
        json.dump(result, json_out, indent=4)

def exporter(nout, jout, urls):
    """
    Invokes the function according to the condition
    """
    if nout:
        normal_output(nout, urls)
    elif jout:
        json_output(jout,urls)