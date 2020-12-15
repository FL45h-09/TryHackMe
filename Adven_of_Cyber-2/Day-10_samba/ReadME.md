#Day-10
....................................................................
====================================================================
Day 10: Don't be so sElfish - Prelude

The Best Festival Company (TBFC) has since upscaled its IT infrastructure after last year's attack for all the other elves to use, including a VPN server and a few other services. You breathe a sigh of relief..."That's it, Me, Elf McEager saved the Christmas of 2020! I can't wait to---"

#But suddenly, a cold shiver runs down your spine, interrupting your monologue...

You suddenly recall that Elf McSkidy had set up a Samba file server just before the attack occurred - could this have been hacked too?!  What about our data...Oh no, quick! Find out what usernames may have been leaked and attempt to login to the server yourself, noting down any vulnerabilities found to report back to Elf McSkidy.
====================================================================
....................................................................


we can use enum4linux to find the users and shared folders on the sabma server.

#enum4linux -U 10.10.117.79

Above command will list the all users associated with this samba server.

#enum4linux -S 10.10.117.79

Above command will list the all Shared folders associated with this samba server.

....................................................................
====================================================================
....................................................................

Now lets try to connect to the Samba server. using the follwing commands.
and find out the user which has no password by just pressing enter on when password is asked.

#smbclient //10.10.117.79/tbfc-santa

#1 Using enum4linux, how many users are there on the Samba server (10.10.117.79)?
	Ans: 3

#2 Now how many "shares" are there on the Samba server?
	Ans: 4

#3 Use smbclient to try to login to the shares on the Samba server (10.10.117.79). What share doesn't require a password?
	Ans: tbfc-santa

#4 Log in to this share, what directory did ElfMcSkidy leave for Santa?
	Ans: jingle-tunes
....................................................................
====================================================================