#!/usr/bin/python3
"""
script to send post request to passed url with email and display
body as response
"""

if __name__ == "__main__":
    import sys
    import requests

    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
