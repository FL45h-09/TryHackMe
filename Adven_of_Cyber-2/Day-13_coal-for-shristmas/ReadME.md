#Day-13
....................................................................
====================================================================
Day 13: Coal For Christmas

Prove these sysadmins deserve coal for Christmas!
====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------
lets nmap the target to get some basic enumeratioon going.
nmap -A -sC -sV -oN intial 10.10.206.126


....................................................................
====================================================================
....................................................................

#1	What is the version number of the web server?
	Ans: 9.0.17

#2	What CVE can be used to create a Meterpreter entry onto the machine? (Format: CVE-XXXX-XXXX)
	Ans: CVE-2019-0232

#3	Set your Metasploit settings appropriately and gain a foothold onto the deployed machine.
	Ans: No answer needed.

#4	What are the contents of flag1.txt
	Ans: thm{whacking_all_the_elves}

#5	Looking for a challenge? Try to find out some of the vulnerabilities present to escalate your privileges!
	Ans: use post/windows/excalate/getsystem

....................................................................
====================================================================