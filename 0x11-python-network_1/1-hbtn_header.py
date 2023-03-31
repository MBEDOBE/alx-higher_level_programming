#!/usr/bin/python3
"""
Script that sends a request to given url
displays the value of X-Request-Id variable
"""


if __name__ == "__main__":
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as reply:
        url_res=reply.info()
        print(url_res['X-Request-Id'])
