#!/usr/bin/env python3
from sympy import root
from Crypto.Util.number import inverse, long_to_bytes

p= 7804787 
q= 7804789
e = 65537
c=33663314778546
n=p*q


phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(d)
m = pow(c, d, n)
print(m)

