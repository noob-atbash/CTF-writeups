---
layout: default
---


## CHALLENGE - 5 (WEAK-DES ATTACK)

In this challenge we were given a python script and the **output.txt** file : 

```
kIi6qSDhcSVErHbkpy/M1hRHfDpr8TiaGbAIrKUXooxSXwNnaeJgTQ==
```
<code>ques.py</code>

```py
from Crypto.Cipher import DES
import base64
from FLAG import flag


def pad(plaintext):
    while len(plaintext) % 8 != 0:
        plaintext += "*"
    return plaintext

def enc(plaintext,key):
    cipher = DES.new(key, DES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(plaintext))


key = "##############".decode("hex")
plaintext = pad(flag)
print enc(plaintext,key)

```
A quick glance at the code (and the challenge title) tells us that we’re dealing with Data Encryption Standard (DES) utilizing ELECTRONIC CODE BOOK (ECB) mode.

My first thought was just to try and bruteforce the key but it didn’t work so I do some more research and looked a little deeper into DES Attacks. I quickly came across an [article](https://crypto.stackexchange.com/questions/7938/may-the-problem-with-des-using-ofb-mode-be-generalized-for-all-feistel-ciphers) that proved to be very helpful.

From the article it was clear that it was kinda weak key DES problem.

```py
0x0000000000000000
0xFFFFFFFFFFFFFFFF
0xE1E1E1E1F0F0F0F0
0x1E1E1E1E0F0F0F0F

```
So lets a write a python script to solve our problem: 

```py
from Crypto.Cipher import DES
from base64 import *

f = open('output.txt', 'rb')
ciphertext = b64decode(f.read())
f.close()

KEY=b'\x00\x00\x00\x00\x00\x00\x00\x00'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b'\x1E\x1E\x1E\x1E\x0F\x0F\x0F\x0F'
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xE1\xE1\xE1\xE1\xF0\xF0\xF0\xF0"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

KEY=b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
a = DES.new(KEY, DES.MODE_ECB)
plaintext = a.decrypt(ciphertext)
print (plaintext)

```

### ASCWG{Welcome_to_des_weak_key_attack}