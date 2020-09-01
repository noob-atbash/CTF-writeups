---
layout: default
---

## MEMORY 1

**Flag is : FwordCTF{computername_user_password}**

```bash

$ volatility -f foren.raw  --imageinfo         # to see the profile name
$ volatility -f foren.raw  --profile=Win7SP0x64  hivelist  # to see the available hivelist
$ volatility -f foren.raw --profile=Win7SP0x64 printkey -o 0xfffff8a000024010 -K "ControlSet001\Control\ComputerName\ComputerName"
$ volatility -f foren.raw --profile=Win7SP1x64 hashdump #all poosible pass
$ volatility --plugins=/home/utilidades/plugins-vol -f foren.raw --profile=Win7SP1x64 mimikatz  #user name

```

## MEMORY 2

**I had a secret conversation with my friend on internet. On which channel were we chatting?**

```bash
$ volatility -f foren.raw --profile=Win7SP1x64 yarascan -Y "FwordCTF{" -p 3700,3752,2560,3304,3304,3528,616,540,3816,2516,3992
$ strings foren.raw | grep "Fword" # alternative

```


## MEMORY 3

**He sent me a secret file , can you recover it ? PS: NO BRUTEFORCE NEEDED FOR THE PASSWORD**

while grepping the Fword in previous i noticed some links and pass.

```bash
$ strings foren.raw | grep "FwordCTF{"
```
I got this link

https://gofile.io/d/k2RkIS

and this password : fw0rdsecretp4ss

opening the link i got a zip which was password protected, opening the file with that password i got the flag.

## MEMORY 4

**Since i'm a geek, i hide my secrets in weird places**

```bash
$ volatility -f foren.raw --profile=Win7SP1x64 printkey -o 0xfffff8a0033fe410

...
Registry: \Device\HarddiskVolume1\Boot\BCD
Key name: NewStoreRoot (S)
Last updated: 2020-08-26 09:10:18 UTC+0000

Subkeys:
  (S) Description
  (S) Objects

Values:
----------------------------
Registry: \??\C:\Users\SBA_AK\ntuser.dat
Key name: CMI-CreateHive{D43B12B8-09B5-40DB-B4F6-F6DFEB78DAEC} (S)
Last updated: 2020-08-26 09:11:20 UTC+0000

Subkeys:
  (S) AppEvents
  (S) Console
  (S) Control Panel
  (S) Environment
  (S) EUDC
  (S) FLAG
  (S) Identities
  (S) Keyboard Layout
  (S) Network
  (S) Printers
  (S) Software
  (S) System
  (V) Volatile Environment

Values:
----------------------------
Registry: \??\C:\Users\SBA_AK\AppData\Local\Microsoft\Windows\UsrClass.dat
...
# One particular registry has a FLAG subkey which obviously interesting.

$ volatility -f foren.raw --profile=Win7SP1x64 printkey -o 0xfffff8a0033fe410 -K 'FLAG'


Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \??\C:\Users\SBA_AK\ntuser.dat
Key name: FLAG (S)
Last updated: 2020-08-25 18:45:05 UTC+0000

Subkeys:

Values:
REG_SZ                        : (S) FwordCTF{hiding_secrets_in_regs}

```


## MEMORY 5

**I'm an artist too, i love painting. I always paint in these dimensions 600x300**

```bash
$ volatility -f foren.raw  --profile=Win7SP0x64  pslist

...
0xfffffa8019ac0640 chrome.exe             3992   3700     14      216      1      0 2020-08-26 09:13:33 UTC+0000

0xfffffa8019bf2060 wuauclt.exe            1876    900      3       98      1      0 2020-08-26 09:13:33 UTC+0000

0xfffffa801adeaa40 mspaint.exe            1044   1000      7      133      1      0 2020-08-26 09:20:28 UTC+0000

0xfffffa8019bc0b00 svchost.exe            3284    488      7      110      0      0 2020-08-26 09:20:28 UTC+0000

0xfffffa8019bf7060 DumpIt.exe             1764   1000      2       52      1      1 2020-08-26 09:22:18 UTC+0000
...

# simply  dumped the memory for mspaint.exe with PID 1044.

$ volatility -f foren.raw  --profile=Win7SP0x64  memdump -p 1044 --dump-dir=dirname

```


{% include disqus.html %}