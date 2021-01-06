#Day-23
....................................................................
====================================================================
#Day 23	: The Grinch strikes again! - Story:

The mayhem at Best Festival Company continues. McEager receives numerous emails and phone calls about a possible ransomware attack affecting all the endpoints in the network. McEager knows that the endpoints which are infected with the malware don't have any backup copies but luckily on his workstation he has backups enabled.

Task: Investigate the malware and restore the files to their original state.

====================================================================
....................................................................
#Steps I aquire to gain answers:
----------------------------------

Logged in with Remmina using RDP protocol.

1st we need to do some changes in prefenreces in remmina:

go in preferences>RDP

and change the Quality setting: poor(fastest)

and chech the wallpaper box.

Now we are ready to go.

Server		 : 10.10.56.160
User name    : Administrator
User password: sn0wF!akes!!!
color Depth	 : remoteFX(32bpp)

So we loggied in to the machine.

now we found the task scheduler on the task bar by looking at it we found there are 2 custome tasks one is for ransomeware and another is for VSS.

So on the desktop we found the ransomeware note in which there was a base64 encoded bitcoin address.

#bitcoin Address: bm9tb3JlYmVzdGZlc3RpdmFsY29tcGFueQ==

So using cyberchef we decrypted that addres and we found our 1st answer.

then we found that the extention for the encrypted files are .grich 

then we look at the task scheduler and we found the suspicious task wich is ransomeware task.


and by inspecting that task we found the exact location for the ransomeware.

then we look at the another scheduled task which is VSS. And we found its ShadowCopyVolume ID.


now lets open the disk manager and look at the volumes in the machine and we found the hidden volume which is not located in the file manager. so lets assign the later to that volume and lets make it visible on file manager.

so now that its visible on file manager lets enumerate that. and lets turn on the hidden option so we can see the hidden files and folders in it.

and by that we found one hidden folder and we got our 6th answer.

now there is a password in it which is our last answer.

master Password: m33pa55w0rdIZseecure!

...............................................................
====================================================================
....................................................................

#1	Decrypt the fake 'bitcoin address' within the ransom note. What is the plain text value?
	Ans: nomorebestfestivalcompany

#2	At times ransomware changes the file extensions of the encrypted files. What is the file extension for each of the encrypted files?
	Ans: .grinch

#3	What is the name of the suspicious scheduled task?
	Ans: opidsfsdf

#4	Inspect the properties of the scheduled task. What is the location of the executable that is run at login?
	Ans: C:\users\administrator\desktop\opidsfsdf.exe

#5	There is another scheduled task that is related to VSS. What is the ShadowCopyVolume ID?
	Ans: 7a9eea15-0000-0000-0000-010000000000

#6	Assign the hidden partition a letter. What is the name of the hidden folder?
	Ans: Confidential

#7	Right-click and inspect the properties for the hidden folder. Use the 'Previous Versions' tab to restore the encrypted file that is within this hidden folder to the previous version. What is the password within the file?
	Ans: m33pa55w0rdIZseecure!

....................................................................
====================================================================