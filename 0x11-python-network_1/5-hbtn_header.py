#!/usr/bin/python3
"""
script that takes in a url to send a request to the url
and display the values of the variable X-Request-Id
"""


if __name__ == '__main__':
    import sys
    import requests
    try:
        response = requests.get(sys.argv[1])
        print(response.headers.get('X-Request-Id'))
    except Exception:
        pass
