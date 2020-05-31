#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pwn
from word2number import w2n
import socket


def words_to_symbol(str):
    if str == "plus":
        return("+")

    elif str == 'minus':
        return("-")

    elif str == "divided-by":
        return("//")

    elif str == "multiplied-by":
        return("*")
    else:
        return(str)




def words_to_number(str):
    list = str.split()
    list[0] = w2n.word_to_num(list[0])
    list[2] = w2n.word_to_num(list[2])
    str = words_to_symbol(list[1])
    return ("{} {} {}".format(list[0],str,list[2]))


r = pwn.remote('chals20.cybercastors.com', 14429)

r.recvline_contains('Hit <enter> when ready.')
r.sendline()
while True:
    try :
        s = r.recvline(False)
        s = s.decode('utf-8')
        print (s)
        if s.endswith('?'):

            # filtering the actual question

            s = words_to_number(s[8:-2])
            answer = str(eval(s))
            print (answer)
            r.sendline(answer)
    except:
        # after the EOF is received it will receive data upto '}'
        print(r.recvuntil('}').decode('utf-8'))
        break
