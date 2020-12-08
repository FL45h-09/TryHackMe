#Blaster

#A blast from the past!
-----------------------------------------


export ip=10.10.71.106


task-1:
------------------------------------------
 	
Deploy the machine!
==========================================

Task-2
------------------------------------------

#1: How many ports are open on our target system?

ans: 2
==================================================

#2: Looks like there's a web server running, what is the title of the page we discover when browsing to it?

Ans: IIS Windows Server
==================================================

#3: Interesting, let's see if there's anything else on this web server by fuzzing it. What hidden directory do we discover?

Ans: /retro
===================================================

#4: Navigate to our discovered hidden directory, what potential username do we discover?

Ans: wade
===================================================

#5: Crawling through the posts, it seems like our user has had some difficulties logging in recently. What possible password do we discover?

Ans: parzival
===================================================

#6: Log into the machine via Microsoft Remote Desktop (MSRDP) and read user.txt. What are it's contents?

Ans: THM{HACK_PLAYER_ONE} (Use xrdp in kali.)
===================================================

Task-3:

---------------------------------------------------

#1: When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?

Ans: 
====================================================

#2: When enumerating a machine, it's often useful to look at what the user was last doing. Look around the machine and see if you can find the CVE which was researched on this server. What CVE was it?

Ans:
=====================================================

#3: Research vulnerability and how to exploit it. Exploit it now to gain an elevated terminal!

Ans: 
=====================================================

#4: Now that we've spawned a terminal, let's go ahead and run the command 'whoami'. What is the output of running this?

Ans: 
=====================================================

#5: Now that we've confirmed that we have an elevated prompt, read the contents of root.txt on the Administrator's desktop. What are the contents? Keep your terminal up after exploitation so we can use it in task four!

Ans: 
======================================================

Task-4:

------------------------------------------------------

#1: 