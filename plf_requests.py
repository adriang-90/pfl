# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Filename: password_checker.py

"""PLC is a simple password leak checker that checks if your password has ever been leaked."""

__version__ = '0.1'
__author__ = 'Adrian Gąsior'

import requests
import hashlib
import sys


def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fethcing: {res.status_code}, check the API and try again')
    return res


def get_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_data(password):
    hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    first_5_hashed, rest = hashed_password[:5], hashed_password[5:]
    response = req_api_data(first_5_hashed)
    return get_leaks_count(response, rest)


def mainy(password):
    count = pwned_api_data(password)
    if count:
        return f'Your password was found {count} times... Consider changing your password!!'
    else:
        return f'Your password was NOT found. This is a good password. Carry on!'
