#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).
If an HTTP error occurs, it prints: Error code: followed by the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

