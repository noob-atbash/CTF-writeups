#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check():
    bytes_object = bytes. fromhex("636173746f72734354467b72317854795f6d316e757433735f67745f73317874795f6d316e757433737d")
    ascii_string = bytes_object.decode("ASCII")
    print(ascii_string)

check()
