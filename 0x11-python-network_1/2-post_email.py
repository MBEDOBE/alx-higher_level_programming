#!/usr/bin/python3
"""
script that takes in a url and an email, sends a POST request
to the url with the email as parameter and displays body of the
response
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url_ = sys.argv[1]
    email_ = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email_)
    email = email.encode('ascii')
    url_req = urllib.request.Request(url_, email)

    with urllib.request.urlopen(url_req) as response:
        url_res = response.read()
    output = url_res.decode('utf-8')
    print(output)
