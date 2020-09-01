---
layout: default
---

## BG & BD !

**Best Gift and Best Day !**

```py 
from Crypto.Util.number import *
import math
from sympy import lcm 
import random
from fractions import gcd 
from sympy import nextprime
from pwn import xor
from secret import p_1,q_1,flag

def verify_keys(a,b):
	while True:
		if a%4==3:
			while b%4!=3:
				b=nextprime(b)
			return a,b
		if b%4==3:
			while a%4!=3:
				a=nextprime(a)
			return a,b
		a,b=nextprime(a),nextprime(b)
	
def enc1(n,e,msg):
	m=int(msg.encode('hex'),16)
	return pow(m,e,n)

def encode(msg):
	enc_msg=""
	for i in msg:
		enc_msg+=bin(ord(i))[2:].zfill(8)
	return enc_msg

def enc2(msg,bs,mds):
	while len(msg)%bs!=0:
		msg='0'+msg
	ll=len(msg)/bs
	r=3945132
	x=pow(r,2,mds)
	c = ''
	for i in range(ll):
		x=pow(x,2,mds)
		p=(bin(x)[2:])[-bs:]
		c_i=int(p,2)^int(msg[i*bs:(i+1)*bs],2)
		ci_bin = format(c_i, '0' + str(bs) + 'b')
		c+=ci_bin
	return c,pow(x,2,mds)


n=p_1*q_1
e=17742461742896634972201474241931685701682825423273435469196581493593083245061146905518481601646582623355393811189032402488804067701439209191772750727581718922909269638936474927145555944487152988216781157681122522177270474504549932191814852246849976334482284151493985991827502940015843682072459462031659332887

part1=flag[:len(flag)/2]
part2=flag[len(flag)/2:]

cipher1=enc1(n,e,part1)
print (cipher1)

p_2,q_2=verify_keys(p_1,q_1)
N=p_2*q_2

block_size=int(math.log(int(math.log(N,2)),2))

cipher2,xt=(enc2(encode(part2),block_size,N))

print (cipher2,xt)


#n : 136925867715334350539351541819374303153581861883077425871381479619256902280896182751175418274848819117804106313526390171733172646719203781502341411544996240718046559322020330755493739123717974336861438650061159088512867158495809372652057009979517497499951599965613535967213529497308200114836792389883404448987
#Cipher 1 : 46282600628982824130530839707152802257095678655388901777970530297126873677669029302844975736419114037407828011895452774978714646752289839556387176301641119447701609034322702222708553203047498652811019927150942380861621605039714510498733535604972160616786208389979609391313009722848684563568437967800442928084
#(cipher2,xt) : ('101110100011010000110010100100000011001110110001010101100101000000100111011010010010110101000101000110000100011001001100111011111011101001110111100001100011101010101111101100001000010111111000110110110010110100000001001011100010011000110100111100001100111001101110001111001100010001001111100110110110100001011100011100110101001000011100100011011110011000010100110010100111000010101101110101011100010110000100001101101101001111000101011100101100100110110011101000100010101000010001010010110110101011111101110011101110010000101001000111000000100100001010110111001011110001010100100001101111010010111101111001001001111010001100000111000010000100110101100010001111100011111100100100001010010100111010100010000101110000110101000101100', 99938901144293305318474508248429453175561082362898230514299720558762394911631823304146558717537729838080951066313213321374755623652896593453644503184122276925455269140340267427068200657877772040554093186417385902385500879519631051754226252925525926019109245833691317900888626583890623823019289563531254979763)
```

So a quite big generator script and with cool description if you give a cursory glance it easy to figure out that the 1st part is RSA attack and since Big E could means two attacks,first wiener second and second the Boneh Durfee attack but since BD in description it become crystal clear that its  Boneh Durfee attack and it's stronger attack so let move ahead  with the evergreen [sage script](https://github.com/mimoo/RSA-and-LLL-attacks/blob/master/boneh_durfee.sage) to get **d** so just set the params and run the code 

```py
d = 23974584842546960047080386914966001070087596246662608796022581200084145416583

```

Once you get **d** you can easily recover **p** and **q** take help of the [github-gist](https://gist.github.com/ddddavidee/b34c2b67757a54ce75cb)

```py
p = 11391686090403905599695015583829755003551766728158057028281938682097322841603835874354540607209988671617182359012432600907514677996087087987893334356043831
q = 12019806956467800913778611206246062087922374347970383926984004278168670921911203657163080865199043522716298571169006826814578568813815787765574990776254077

```

Now we can proceed to the next part of the problem for curosity I just check the first ciphertext $c_1$ and it's just have this message :

>well its not a long story to be told , you are on the right path , after darkness you find


I was unable to solve this problem this during the CTF I was stuck on the second part : 

Second part was actually [Blum–Goldwasser cryptosystem](https://en.wikipedia.org/wiki/Blum%E2%80%93Goldwasser_cryptosystem) (aka BG)

So lets take breif overview on this cryptosystem as this will be new for many of us : 

### KEY GENERATION 

1. Choose two large distinct prime numbers p and q such that $p \equiv 3\pmod{4}   \\ and\\ $$q \equiv 3\pmod{4}$
2. compute $n = pq$

The easiest thing is like we just need to take out piceses from generator code and make solver script for us for the validation of ket-generation part just use this : 

```py 

def verify_keys(a,b):
	while True:
		if a%4==3:
			while b%4!=3:
				b=nextprime(b)
			return a,b
		if b%4==3:
			while a%4!=3:
				a=nextprime(a)
			return a,b
		a,b=nextprime(a),nextprime(b)

p2, q2 = verify_keys(p, q)
N = p2 * q2

```

## ENCRYPTION 


A message $M$ is encrypted with the public key $n$ as follows:

1. Compute the block size in bits, ${\displaystyle h=\lfloor log_{2}(log_{2}(n))\rfloor }$
2. Convert $M$ to a sequence of $t$ blocks ${\displaystyle m_{1},m_{2},\dots ,m_{t}}$, where each block is $h$ bits in length.
3. Select a random integer $r < n$ 
4. Compute $x_{0} = r^2 mod n$
5. For $i$ from $1$ to $t$ 
    1. Compute ${\displaystyle x_{i}=x_{i-1}^{2}{\bmod {n}}}$
    2. Compute ${\displaystyle p_{i}=}$ the least significant $h$ bits of $x_{i}$.
    3. Compute ${\displaystyle c_{i}=m_{i}\oplus p_{i}}$
6. Finally, compute ${\displaystyle x_{t+1}=x_{t}^{2}{\bmod {n}}}$

So, for this part we need to have block size so just using this part from the genrator script 


```py

block_size=int(math.log(int(math.log(N,2)),2))

assert len(c2) % block_size == 0

r=3945132 #also have r 

```

```py
>>> import math
>>> N = 136925867715334350539351541819374303153581861883077425871381479619256902280896182751175418274848819117804106313526390171733172646719203781502341411544996240718046559322020330755493739123717974336861438650061159088512867158495809372652057009979517497499951599965613535967213529497308200114836792389883404448987
>>> block_size=int(math.log(int(math.log(N,2)),2))
>>> block_size
9
```

## DECRYPTION 

An encrypted message ${\displaystyle (c_{1},c_{2},\dots ,c_{t},x)}$  can be decrypted with the private key ${\displaystyle (p,q)}$ as follows:


1. Compute ${\displaystyle d_{p}=((p+1)/4)^{t+1}{\bmod {(p-1)}}}$
2. Compute ${\displaystyle d_{q}=((q+1)/4)^{t+1}{\bmod {(q-1)}}}$ .
3. Compute ${\displaystyle u_{p}=x^{d_{p}}{\bmod {p}}}$.
4. Compute ${\displaystyle u_{q}=x^{d_{q}}{\bmod {q}}}$.
5. Using the Extended Euclidean Algorithm, compute $r_{p} and r_{q}$  such that ${\displaystyle r_{p}p+r_{q}q=1}$
6. Compute ${\displaystyle x_{0}=u_{q}r_{p}p+u_{p}r_{q}q{\bmod {n}}}$This will be the same value which was used in encryption $x_{0}$ can then used to compute the same sequence of $x_{i}$ values as were used in encryption to decrypt the message, as follows.
7. For $i$ from $1 \\to t$
   1. Compute ${\displaystyle x_{i}=x_{i-1}^{2}{\bmod {n}}}$.
   2. Compute $p_{i}$ the least significant ${\displaystyle h} bits of {\displaystyle x_{i}}$.
   3. Compute ${\displaystyle m_{i}=c_{i}\oplus p_{i}}$
8. Finally, reassemble the values ${\displaystyle (m_{1},m_{2},\dots ,m_{t})}$ into the message $M$

For the decryption part just look only the last and  the **encode(msg)** , **enc2(msg,bs,mds)** function which actually splits input into 9-bit chunks and XORs them with some keystream generated by squaring some seed modulo $p_2*q_2$. The operation is reversible, so  just copy the code  that from the original source with minor changes

```py
x = pow(r,2,N)
m = ''
for i in range(0, len(c2), block_size):
    x = pow(x,2,N)
    c = int(c2[i:i+block_size], 2)
    p = int(bin(x)[2:][-block_size:],2)
    m += format(c ^ p, '0' + str(block_size) + 'b')

```
> If you don't get this part just see the [example](https://en.wikipedia.org/wiki/Blum%E2%80%93Goldwasser_cryptosystem#Example) from wikipedia  how ir works.


Now Time to join all the pisces . 

```py 
from Crypto.Util.number import *
from sympy import nextprime
import gmpy2, math

n = 136925867715334350539351541819374303153581861883077425871381479619256902280896182751175418274848819117804106313526390171733172646719203781502341411544996240718046559322020330755493739123717974336861438650061159088512867158495809372652057009979517497499951599965613535967213529497308200114836792389883404448987
e = 17742461742896634972201474241931685701682825423273435469196581493593083245061146905518481601646582623355393811189032402488804067701439209191772750727581718922909269638936474927145555944487152988216781157681122522177270474504549932191814852246849976334482284151493985991827502940015843682072459462031659332887
c1 = 46282600628982824130530839707152802257095678655388901777970530297126873677669029302844975736419114037407828011895452774978714646752289839556387176301641119447701609034322702222708553203047498652811019927150942380861621605039714510498733535604972160616786208389979609391313009722848684563568437967800442928084
xt = 99938901144293305318474508248429453175561082362898230514299720558762394911631823304146558717537729838080951066313213321374755623652896593453644503184122276925455269140340267427068200657877772040554093186417385902385500879519631051754226252925525926019109245833691317900888626583890623823019289563531254979763
c2='101110100011010000110010100100000011001110110001010101100101000000100111011010010010110101000101000110000100011001001100111011111011101001110111100001100011101010101111101100001000010111111000110110110010110100000001001011100010011000110100111100001100111001101110001111001100010001001111100110110110100001011100011100110101001000011100100011011110011000010100110010100111000010101101110101011100010110000100001101101101001111000101011100101100100110110011101000100010101000010001010010110110101011111101110011101110010000101001000111000000100100001010110111001011110001010100100001101111010010111101111001001001111010001100000111000010000100110101100010001111100011111100100100001010010100111010100010000101110000110101000101100'
p = 11391686090403905599695015583829755003551766728158057028281938682097322841603835874354540607209988671617182359012432600907514677996087087987893334356043831
q = 12019806956467800913778611206246062087922374347970383926984004278168670921911203657163080865199043522716298571169006826814578568813815787765574990776254077


def verify_keys(a,b):
	while True:
		if a%4==3:
			while b%4!=3:
				b=nextprime(b)
			return a,b
		if b%4==3:
			while a%4!=3:
				a=nextprime(a)
			return a,b
		a,b=nextprime(a),nextprime(b)


p2, q2 = verify_keys(p, q)
N = p2 * q2

block_size=int(math.log(int(math.log(N,2)),2))

assert len(c2) % block_size == 0

r=3945132
x = pow(r,2,N)
m = ''
for i in range(0, len(c2), block_size):
    x = pow(x,2,N)
    c = int(c2[i:i+block_size], 2)
    p = int(bin(x)[2:][-block_size:],2)
    m += format(c ^ p, '0' + str(block_size) + 'b')

print(long_to_bytes(int(m, 2)).decode())

```
### Flag: FwordCTF{boneh_and_blum?_mix3d_but_good_j0b!!}