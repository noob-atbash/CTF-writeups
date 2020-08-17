---
layout: default
---

# CRYPTO

### Rivest Shamir Adleman

A simple RSA problem you can also use [rsactftool](https://github.com/Ganapati/RsaCtfTool) since the given numbers are are small or you can use python ninja techniques and write script to do this for you I got the factors using [alpetron](https://www.alpertron.com.ar/ECM.HTM)

```
n = 408579146706567976063586763758203051093687666875502812646277701560732347095463873824829467529879836457478436098685606552992513164224712398195503564207485938278827523972139196070431397049700119503436522251010430918143933255323117421712000644324381094600257291929523792609421325002527067471808992410166917641057703562860663026873111322556414272297111644069436801401012920448661637616392792337964865050210799542881102709109912849797010633838067759525247734892916438373776477679080154595973530904808231
e = 65537
c = 226582271940094442087193050781730854272200420106419489092394544365159707306164351084355362938310978502945875712496307487367548451311593283589317511213656234433015906518135430048027246548193062845961541375898496150123721180020417232872212026782286711541777491477220762823620612241593367070405349675337889270277102235298455763273194540359004938828819546420083966793260159983751717798236019327334525608143172073795095665271013295322241504491351162010517033995871502259721412160906176911277416194406909

```


```py

from Crypto.Util.number import inverse, long_to_bytes


n = 408579146706567976063586763758203051093687666875502812646277701560732347095463873824829467529879836457478436098685606552992513164224712398195503564207485938278827523972139196070431397049700119503436522251010430918143933255323117421712000644324381094600257291929523792609421325002527067471808992410166917641057703562860663026873111322556414272297111644069436801401012920448661637616392792337964865050210799542881102709109912849797010633838067759525247734892916438373776477679080154595973530904808231
e = 65537
c = 226582271940094442087193050781730854272200420106419489092394544365159707306164351084355362938310978502945875712496307487367548451311593283589317511213656234433015906518135430048027246548193062845961541375898496150123721180020417232872212026782286711541777491477220762823620612241593367070405349675337889270277102235298455763273194540359004938828819546420083966793260159983751717798236019327334525608143172073795095665271013295322241504491351162010517033995871502259721412160906176911277416194406909
p = 15485863
q = 26384008867091745294633354547835212741691416673097444594871961708606898246191631284922865941012124184327243247514562575750057530808887589809848089461174100421708982184082294675500577336225957797988818721372546749131380876566137607036301473435764031659085276159909447255824316991731559776281695919056426990285120277950325598700770588152330565774546219611360167747900967511378709576366056727866239359744484343099322440674434020874200594041033926202578941508969596229398159965581521326643115137




phi = (p - 1) * (q - 1)
d = inverse(e, phi)


m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag)

```

### csictf{sh0uld'v3_t4k3n_b1gg3r_pr1m3s}


## MORDEN CLULESS CHILD 

CHALLENGE DESCRIPTION

```
I was surfing the crimson wave and oh my gosh I was totally bugging. I also tried out the lilac hair trend but it didn't work out. That's not to say you are any better, you are a snob and a half. But let's get back to the main question here- Who am I? (You don't know my name)

Ciphertext = "52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e" (hex) Key = "12123"

``` 

I don't know that what their challenege description means I just focused on ciphertext and key and  considered it as XOR problem but if you blindly try to solve the XOR with key it won't work if you analyse the cipher text pattern you will find that **f** is being used for spacing so simply remove the **f** from ciphertext.
```py
>>> c='52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e'
>>> c.replace("f","")
'52415851475749485d466e5343576c506d53534058516e425643415e5c4e'
>>> 
```
To crosscheck that everything is alright you can use basic XOR properties : 

```py
flag = bytes.fromhex('52415851475749485d466e5343576c506d53534058516e425643415e5c4e')
print(xor(flag, 'csictf{'.encode()))
b"1212312+./\r'%,\x0f#\x040'&#2\x1d+57'%?="
```
> Sice we got the key 1212312 means we are right path as key has cyclic property key(12123) is also correct , Now just solve it : 

```py
>>> from pwn import xor
>>> flag = bytes.fromhex('52415851475749485d466e5343576c506d53534058516e425643415e5c4e')
>>> print(xor(flag, '12123'.encode()))
b'csictf{you_are_a_basic_person}'
>>> 

```
### csictf{you_are_a_basic_person}

### LITTLE RSA 

These were the values for RSA and their was a password protected zip file, so we need to decode c which

```bash

The flag.zip contains the flag I am looking for but it is password protected. The password is the encrypted message which has to be correctly decrypted so I can useit to open the zip file. I tried using RSA but the zip doesn't open by it. Can you help me get the flag please?

```

These were the values for RSA and their was a password protected zip file, so basically a easy peasy RSA 
```
c=32949
n=64741
e=42667

```

```py
c=32949
n=64741
e=42667
p = 101 
q = 641

phi = (p - 1) * (q - 1)
d = inverse(e, phi)


m = pow(c, d, n)
print(m)
flag = long_to_bytes(m).decode()
print(flag)

```
The script print the value **m = 18429**  and it cannot decode c  because  the problem here is that the second byte is **0xfd** which is not in the ascii range and therefore can't be decoded so in general for comparison "hello" is 448378203247, "he" is 26725 so **c**
so it would be max  2 chars but since it's not possible so **m** is the password for the zip file

### csictf{gr34t_m1nds_th1nk_4l1ke}

## QUICK MATH

```
Ben has encrypted a message with the same value of 'e' for 3 public moduli - n1 = 86812553978993 n2 = 81744303091421 n3 = 83695120256591 and got the cipher texts - c1 = 8875674977048 c2 = 70744354709710 c3 = 29146719498409. Find the original message. (Wrap it with csictf{})
```

If you are regular crypto guy you can tell that it's an **hastad attck** by seeing tha challenge description and if you don't kno give a read to this [post](https://crypto.stackexchange.com/questions/52504/deciphering-the-rsa-encrypted-message-from-three-different-public-keys) it will be clear.

So python our bestfriend can give you the flag this is my script :

```py
from sympy.ntheory.modular import crt
from gmpy2 import iroot


n = [ 86812553978993,81744303091421,83695120256591 ]
c = [8875674977048,70744354709710, 29146719498409 ]


e=3

  
resultant, mod = crt(n,c)
value, is_perfect = iroot(resultant,e)
if is_perfect:
   print(value)

#683435743464
```

```py
>>> bytearray.fromhex("683435743464").decode()
'h45t4d'
```

### csictf{h45t4d}