#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def checkpass():
    _input = input("Enter the password: ")
    key = "promortyusvatofacidpromortyusvato"
    encoded = str.encode(xor(key, _input))
    result = base64.b64encode(encoded, altchars=None)
    if result == b'ExMcGQAABzohNQ0TRQwtPidYAS8gXg4kAkcYISwOUQYS':
        return True
    else:
        return False

def main():
    global access
    access = checkpass()
    if access:
        print("Yeah...okay. You got it!")
    else:
        print("Lol...try again...")

access = False
main()
