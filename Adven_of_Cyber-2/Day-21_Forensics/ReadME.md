#Day-21
....................................................................
====================================================================
#Day 21	: Time for some ELForensics - Story:

One of the 'little helpers' logged into his workstation only to realize that the database connector file has been replaced, and he can't find the naughty list anymore. Furthermore, upon executing the database connector file, a taunting message was displayed, hinting that the file was moved to another location.

McEager has been notified, and he will put the pieces together to find the database connector file.

Watch DarkStar's Video On Solving The Task Here.

Task: Find where the database connector file is hidden using forensic-like investigative techniques.

====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------

Logged in with Remmina using RDP protocol.


Server		 : 10.10.252.139
color Depth	 : remoteFX(32bpp)
User name    : littlehelper
User password: iLove5now!

1st we need to go to DOcuments directory:
#set-location C:\Users\littlehelper\Documents

now lets see the hash from the txt file:
#get-content -Path file.txt

and we found the 1st answer.

to find the deebee.exe file's hash:
#get-filehash -algorithm MD5 deebee.exe

we found the 2nd answer.

now we need to find the hidden flag in the file using string tool:
#c:\Tools\strings64.exe -accepteula deebee.exe

and we found our 3rd answer.

now lets find the 4th and last flag:

1st we need to find the streem of the current file:
#get-item -path deebee.exe -stream *

by the above command we found the following stream:

Stream        : hidedb
Length        : 6144

now lets find the last flag:
#wmic process call create $(resolve-path deebee.exe:hidedb)

and here we found our last flag.



...............................................................
====================================================================
....................................................................

#1	Read the contents of the text file within the Documents folder. What is the file hash for db.exe?
	Ans: 596690FFC54AB6101932856E6A78E3A1

#2	What is the file hash of the mysterious executable within the Documents folder?
	Ans: 5F037501FB542AD2D9B06EB12AED09F0

#3	Using Strings find the hidden flag within the executable?
	Ans: THM{f6187e6cbeb1214139ef313e108cb6f9}

#4	What is the flag that is displayed when you run the database connector file?
	Ans: THM{088731ddc7b9fdeccaed982b07c297c}

....................................................................
====================================================================