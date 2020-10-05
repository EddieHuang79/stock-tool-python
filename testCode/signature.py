#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Signs a URL using a URL signing secret """

import hashlib
import hmac
import base64
import urllib.parse as urlparse
import sys


def sign_url(input_url=None, secret=None):
    """ Sign a request URL with a URL signing secret.
      Usage:
      from urlsigner import sign_url
      signed_url = sign_url(input_url=my_url, secret=SECRET)
      Args:
      input_url - The URL to sign
      secret    - Your URL signing secret
      Returns:
      The signed request URL
  """

    if not input_url or not secret:
        raise Exception("Both input_url and secret are required")

    url = urlparse.urlparse(input_url)

    # We only need to sign the path+query part of the string
    url_to_sign = url.path + "?" + url.query

    # Decode the private key into its binary format
    # We need to decode the URL-encoded private key
    decoded_key = base64.urlsafe_b64decode(secret)
    # print(base64.urlsafe_b64encode(decoded_key))
    # sys.exit()

    # Create a signature using the private key and the URL-encoded
    # string using HMAC SHA1. This signature will be binary.
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)
   
    print(decoded_key)
    sys.exit()

    # Encode the binary signature into base64 for use within a URL
    encoded_signature = base64.urlsafe_b64encode(signature.digest())

    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query

    print(encoded_signature.decode())
    sys.exit()

    # Return signed URL
    return original_url + "&signature=" + encoded_signature.decode()


if __name__ == "__main__":
    input_url = 'http://maps.googleapis.com/maps/api/staticmap?center=25.033443907416395,121.50137440000002&zoom=17&size=800x600&markers=25.0334439,121.5013744&scale=2&format=jpeg&key=AIzaSyAT9oqEZ_8iDLWPdM7yIX7-h2tLN4AcBUs'
    secret = 'TudZaZ29w4dpL-U23QGoqys-gNQ='
    print("Signed URL: " + sign_url(input_url, secret))