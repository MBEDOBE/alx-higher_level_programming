#!/usr/bin/python3
"""
script that fetches url only with requests
"""

if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(response.content.decode()))
    print('\t- content:', response.content.decode())
