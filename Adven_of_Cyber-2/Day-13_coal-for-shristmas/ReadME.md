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
nmap -A -sC -sV -O -oN intial 10.10.148.69

Ok so we found that there is telnet running on port 23.

so lets try to login using telnet.

telnet 10.10.148.69 23

then the username and password was provided there.

lets enumerate some directoris and files to grab some answers.

we found that this version of ubuntu is vulnarable to dirt CoW attack.

lets grab it by searching the small code from coocki_and_milk.txt file.

we cound the .c exploit so there lets compile it using following command:
#gcc -pthread dirty.c -o dirty -lcrypt

now the file is compailes lets run it.

we have got the new user and passwd:

#You can log in with the username 'firefart' and the password '12034rv'.

lets login to that:
su firefart

As we are now root user, now lets go in to the /root directory.

there is a messeage file. lets look in ot it:

Nice work, Santa!

Wow, this house sure was DIRTY!
I think they deserve coal for Christmas, don't you?
So let's leave some coal under the Christmas `tree`!

Let's work together on this. Leave this text file here,
and leave the christmas.sh script here too...
but, create a file named `coal` in this directory!
Then, inside this directory, pipe the output
of the `tree` command into the `md5sum` command.

The output of that command (the hash itself) is
the flag you can submit to complete this task
for the Advent of Cyber!

        - Yours,
                John Hammond


So it says that we have to create a file called cola and pipe the tree in to md5sum

So lets do this.

nano coal

tree | md5sum

now lets make it executable.

chmod _x coal

and now lets run it.

./coal

and we have oour final flag.

....................................................................
====================================================================
....................................................................

#1	Port Scanning
	Ans: No Answer Needed.

#2	What old, deprecated protocol and service is running?
	Ans: telnet

#3	What credential was left for you?
	Ans: clauschristmas

#4	What distribution of Linux and version number is this server running?
	Ans: Ubuntu 12.04

#5	Who got here first?
	Ans: Grunch

#6	What is the verbatim syntax you can use to compile, taken from the real C source code comments?
	Ans: gcc -pthread dirty.c -o dirty -lcrypt

#7	What "new" username was created, with the default operations of the real C source code?
	Ans: firefart

#8	su <user_to_change_to>
	Ans: No Answer needed.

#9	What is the MD5 hash output?
	Ans: 8b16f00dd3b51efadb02c1df7f8427cc

....................................................................
====================================================================