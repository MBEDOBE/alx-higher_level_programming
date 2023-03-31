#!/usr/bin/python3
"""
Script that sends a request to given url
displays the value of X-Request-Id variable
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_res = response.info()
        print(url_res['X-Request-Id'])
