#Title: VulnUniversity.
--------------------------------------------------------------------------
export ip=10.10.169.241
--------------------------------------------------------------------------
Task-1: Deploy the machine.

==========================================================================

Task-2: Reconnaissance 

==========================================================================

#1 	Scan this box: nmap -sV <machines ip>
	Ans: No answer needed.

#2 	Scan the box, how many ports are open?
	Ans: 6

#3 	What version of the squid proxy is running on the machine?
	Ans: http-server-header: squid/3.5.12 | 3.5.12

#4 	How many ports will nmap scan if the flag -p-400 was used?
	Ans: 400

#5 	Using the nmap flag -n what will it not resolve?
	Ans: DNS

#6 	What is the most likely operating system this machine is running?
	Ans: UBUNTU

#7 	What port is the web server running on?
	Ans: 3333

#8 	Its important to ensure you are always doing your reconnaissance thoroughly before progressing. Knowing all open services (which can all be points of exploitation) is very important, don't forget that ports on a higher range might be open so always scan ports after 1000 (even if you leave scanning in the background).
	Ans: No Answer needed.
==========================================================================

Task-3: Locating directories using GoBuster 

==========================================================================
#1 	Lets first start of by scanning the website to find any hidden directories. To do this, we're going to use GoBuster.
	Ans: 

#2 	What is the directory that has an upload form page?
	Ans: /internal/

==========================================================================

Task-4: Compromise the webserver 

==========================================================================

#1 	Try upload a few file types to the server, what common extension seems to be blocked?
	Ans: .php

#2 	To identify which extensions are not blocked, we're going to fuzz the upload form.
	Ans: No answer is needed.

#3	Run this attack, what extension is allowed?
	Ans: .phtml

#4 You should see a connection on your netcat session.
	Ans: No Answer needed.

#5 	What is the name of the user who manages the webserver?
	Ans: bill

#6	What is the user flag?
	Ans: 8bd7992fbe8a6ad22a63361004cfcedb

==========================================================================

Task-5: Privilage Excalation.

=========================================================================



=========================================================================