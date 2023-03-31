#!/usr/bin/python3
"""
Script that takes a letter and post request to url/search_user
"""


if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) > 1:
        q_data = sys.argv[1]
    else:
        q_data = ''
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q_data})

    try:
        result = response.json()
        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
