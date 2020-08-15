---
layout: default
---


# CHALLANGE - 1  (NUMBER THEORY)
--- 
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


Challenge was having the below script : 

```py
flag = open("flag.txt","rb").read()
if len(flag) > 50:
    exit()

a = int.from_bytes(open("flag.txt","rb").read(), byteorder='big')

b = a << 99998
b = str(b)
if not b.endswith('46186384884704143502810449626149776675765629346197308004864280982758330594138478052711607866947764263543620513433238646216483214982856318892731845815726243647558073159634372394623630437969797570363392'):
    exit()

# End OF Challenge

```
>QUICK ANALYSIS

The flag is converted to an integer value and shifted 99998 bits to the left to give the last 199 decimal digits of the value. In other words, the purpose of this problem is to restore the flag value from:

$$c = flag⋅2^{99998}mod10^{199}$$

At first you may try taking the inverse of $$2^{10000}\\ over\\ F_{10^{175}}$$, but that should be impossible because they are not coprime

The correct way is, first think of

$$c=\text{flag}\cdot2^{99998}\bmod5^{199}$$

and, by Euler’s theorem, we can calculate :

$$(2^{99998})^{-1}\bmod5^{199}$$ 
$$=(2^{10000})^{\varphi(5^{199})-1}$$
$$=(2^{99998})^{5^{199}-5^{199}-1}$$


Since $${256}^{50} < 5^{199}$$, this is the only value that can satisfy the equation.

```py
c = 46186384884704143502810449626149776675765629346197308004864280982758330594138478052711607866947764263543620513433238646216483214982856318892731845815726243647558073159634372394623630437969797570363392
mod = 5 ** 199
phi = 5 ** 199 - 5 ** 198
inv = pow(pow(2, 99998, mod), phi - 1, mod)
print(((c * inv) % mod).to_bytes(50, byteorder='big'))

```

### ASCWG{Number_Ther0m_1s_1mportanmt_1n_Crypt0_12387}
--- 

### METHOD  2

$$ C = flag . 2^{99998}$$

> Note that there's no modulo taken here.

On the other hand we know *c*, which is the last 199 digits of *C*, so we can put:

Now we want to calculate 𝑐0 which makes the last 99998 digits of the binary form of C all zero.

Then consider **C'**, which can be obtained by replacing 
$$ c_0\\ as\\  c'_0 = c_0 + 2x $$

Now we get:


$$C'\\ =\\ c'_O\cdot10^{199}+c$$
$$=(c_0+2^{x})\cdot10^{199}+c\ =\\ c_0\cdot10^{199}+c+2^{x}\cdot10^{199} $$ 
$$ = \\ C+5^{199}\cdot2^{x+199} $$

--- 

```py

c = 46186384884704143502810449626149776675765629346197308004864280982758330594138478052711607866947764263543620513433238646216483214982856318892731845815726243647558073159634372394623630437969797570363392

c0 = 0
bit = 1
mask = 1 << 199
while '1' in bin(c0 * 10 ** 199 + c)[-99998:]:
  if (c0 * 10 ** 199 + c) & mask != 0:
    c0 += bit
  bit <<= 1
  mask <<= 1
C = c0 * 10 ** 199 + c
flag = (C >> 99998).to_bytes(50, byteorder='big')
print(flag)

```

### ASCWG{Number_Ther0m_1s_1mportanmt_1n_Crypt0_12387}