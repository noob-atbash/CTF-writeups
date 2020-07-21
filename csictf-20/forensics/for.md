# FORENSIC

## GRADIENT SKY 

![](/img/sky.jpg)

The above image was given following the basic commands I got this by binwalk 

```
root@kali:~/ctf/csictf/forensics# binwalk sky.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, little-endian offset of first image directory: 8
918           0x396           JPEG image data, JFIF standard 1.01
295038        0x4807E         RAR archive data, version 5.x

root@kali:~/ctf/csictf/forensics#
```
As results show it has some RAR content on unraring the content I got the flag

### csictf{j0ker_w4snt_happy}


## ARCHED

![](/img/arched.png)

As starting with the classical command to check the file formate and it was a .jpg file

```bash
root@kali:~/Desktop# file arched.png
arched.png: JPEG image data, JFIF standard 1.01, resolution (DPI), density 300x300, segment length 16, baseline, precision 8, 1920x1080, components 3
root@kali:~/Desktop#
```
After renaming it .jpg I run some tools and steghide worked perfectly and I got a flag.zip file.

```bash

root@kali:~/Desktop# steghide extract -sf arched.jpg
Enter passphrase:
wrote extracted data to "flag.zip".
root@kali:~/Desktop#

```
Since it was password protected I use fcrack and everyone's fav rockyou.txt to crack it .

```bash
root@kali:~/Desktop# fcrackzip -u -D -p rockyou.txt flag.zip


PASSWORD FOUND!!!!: pw == kathmandu
root@kali:~/Desktop#
```
After unlocking we got a image which have the flag .

## PANDA
In this question we were given a password protected zip file so by using fcrackzip lets crack it . 
```
root@kali:~/Desktop#  fcrackzip -u -D -p rockyou.txt panda.zip


PASSWORD FOUND!!!!: pw == 2611
```

On extracting the zip file we get two panda images at first I tried a loot of tools but it much easier the flag was in the differnce of the strings of the two images so.

![](/img/pada1.jpg)
![](/img/pada.jpg)

```
root@kali:~/Desktop# strings panda1.jpg > p.txt
root@kali:~/Desktop# strings panda.jpg >  q.txt
root@kali:~/Desktop# diff p.txt q.txt

2c2
< $csi

> $3br
93d92
< ctf{
258d256
< kun-
501d498
< Dfu_w
565c562
< p4nd4}

> i$bI

```

From here it was quite frustrating because you need to guess the flag words however I cracked it.

### csictf{kung_fu_panda}


>Soon updating more