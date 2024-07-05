#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Check if URL and email are provided as arguments
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data to send in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request object
    req = urllib.request.Request(url, data=data)

    # Send the POST request and handle the response
    with urllib.request.urlopen(req) as response:
        # Read the response body
        response_data = response.read().decode('utf-8')

        # Print the response body
        print("Your email is: {}".format(email))
        print(response_data)

