#Day-11
....................................................................
====================================================================
Day 11 - The Rogue Gnome: Prelude

This is it - the moment that Elf McEager has been waiting for. It's the final exam of the Nmap course that he enlisted on during "Day 8 - What's Under the Christmas Tree?". It looks like all that hard work of hitting the books has paid off..."Success!" Elf McEager screams..."the exploit worked! Yippeee!"

Elf McEager has successfully managed to create a reverse shell from the target back to his computer. Little did he know, the real exam begins now...The last stage of the exam requires Elf McEager to escalate his privileges! He spent so much time studying Nmap cheatsheets that he's now drawing a blank...Can you help Elf McEager?

To be the good guy, sometimes you gotta be the bad guy first...
====================================================================
....................................................................

11.7. The "Priv Esc Checklist"

As you progress through your pentesting journey, you will begin to pick up a certain workflow for how you approach certain stages of an engagement. Whilst this workflow is truly yours, it will revolve around some fundamental steps in looking for vulnerabilities for privilege escalation.

    Determining the kernel of the machine (kernel exploitation such as Dirtyc0w)
    Locating other services running or applications installed that may be abusable (SUID & out of date software)
    Looking for automated scripts like backup scripts (exploiting crontabs)
    Credentials (user accounts, application config files..)
    Mis-configured file and directory permissions

Checkout some checklists that can be used as a cheatsheet for the enumeration stage of privilege escalation:

    g0tmi1k 			:https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation

    payatu				:https://payatu.com/guide-linux-privilege-escalation

    PayloadAllTheThings	:https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md#linux---privilege-escalation

Let's confirm this by using find to search the machine for executables with the SUID permission set: 
#find / -perm -u=s -type f 2>/dev/null

....................................................................
====================================================================
....................................................................

#1	What type of privilege escalation involves using a user account to execute commands as an administrator?
	Ans: Vertical

#2	What is the name of the file that contains a list of users who are a part of the sudo group?
	Ans: sudoers

#3	Use SSH to log in to the vulnerable machine like so: ssh cmnatic@10.10.111.249. Input the following password when prompted: aoc2020.
	Ans: No answer needed.

#4	Enumerate the machine for executables that have had the SUID permission set. Look at the output and use a mixture of GTFObins and your researching skills to learn how to exploit this binary. You may find uploading some of the enumeration scripts that were used during today's task to be useful.
	Ans: No answer needed.

#5	Use this executable to launch a system shell as root. What are the contents of the file located at /root/flag.txt?
	Ans: thm{2fb10afe933296592}

....................................................................
====================================================================