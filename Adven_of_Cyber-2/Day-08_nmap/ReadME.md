#Day-8
....................................................................
====================================================================
Day 8: What's Under the Christmas Tree? - Story:

After a few months of probation, intern Elf McEager has passed with glowing feedback from Elf McSkidy. During the meeting, Elf McEager asked for more access to The Best Festival Company's (TBFC's) internal network as he wishes to know more about the systems he has sworn to protect.

Elf McSkidy was reluctant to agree. However, after Elf McEager's heroic actions in recovering Christmas, Elf McSkidy soon thought this was a good idea. This was uncharted territory for Elf McEager - he had no idea how to begin finding out this information for his new responsibilities. Thankfully, TBFC has a wonderful up-skill program covering the use of Nmap for ElfMcEager to enrol in.
====================================================================
....................................................................

#1	When was Snort created?
	Ans: 1998

#2	Using Nmap on MACHINE_IP , what are the port numbers of the three services running?  (Please provide your answer in ascending order/lowest -> highest, separated by a comma).
	Ans: 80,2222,3389
	command: nmap -A -O -sV -sC -oN initial 10.10.219.59
	-A 	For agressive scan.
	-O 	For OS detection
	-sV For version detection
	-sC For Default scripts
	-oN For output the scan result in file called initial

#3	Run a scan and provide the -Pn flag to ignore ICMP being used to determine if the host is up.
	Ans: No answer needed.

#4	Run a scan and provide the -Pn flag to ignore ICMP being used to determine if the host is up
	Ans: No Answer needed.

#5	Use Nmap to determine the name of the Linux distribution that is running, what is reported as the most likely distribution to be running?
	Ans: Ubuntu

#6	Use Nmap's Network Scripting Engine (NSE) to retrieve the "HTTP-TITLE" of the webserver. Based on the value returned, what do we think this website might be used for?
	Ans: blog

#7	Now use different scripts against the remaining services to discover any further information about them.
	Ans: No answer needed.

