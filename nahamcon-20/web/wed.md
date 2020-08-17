---
layout: default
---
# WEB

## Agent-95

![](img/agent-95.png)

The challenge was pretty simple we have to change the agent name to any old **Window-95** version.I googled for some old agent version of windows and used that to get the flag.

![](img/a-95.png)


## Localghost

A simple webpage with peculiar scrolling feature from inspectiing the source code I found a link.

![](img/l1.png)

After opening the url I found huge amount of  hex value.

![](img/l2.png)

Converting the hex into Ascii

![](img/l3.png)

Here we got the flag in base64 encoded form after decoding it we get the flag

![](img/l4.png)


## Phonebook

![](img/p1.png)

After opening the webpage we we were instructed that :

![](img/p.png)

after changing the url phonebook.php we land to :

![](img/phonebook.png)

As the question states *"But you will only get a flag if it is an emergency!"* So I used POSTMAN to send a post request as **emergency=true**

![](img/p2.png)
