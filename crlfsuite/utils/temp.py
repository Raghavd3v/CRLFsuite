# -*- coding: utf-8 -*-

def create_temp_file(urls):
    """
    Creates a resumable file so the user can resume the scan in future
    """
    with open('resumable_data.crlfsuite', 'w+', encoding='utf-8') as temp_file:
        for url in urls:
            temp_file.write(url)
            temp_file.write('\n')
    temp_file.close()