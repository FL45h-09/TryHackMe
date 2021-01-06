#Room-Easy Peasy
....................................................................
====================================================================
#Day 17: Easy peasy


====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------
export IP=10.10.55.207

ports: 80, 6498, 65524

$ip:80/hidden
found 1st flag in page source on: $ip:80/hidden/waterver

User-Agent:*
Disallow:/
Robots Not Allowed
User-Agent:a18672860d0510e5ab6699730763b250 //thats a md5 hash lets crack it

flag{1m_s3c0nd_fl4g}

Allow:/
This Flag Can Enter But Only This Flag No More Exceptions

base62:ObsJmP173N2X6dOrAgEAL0Vu
/n0th1ng3ls3m4tt3r

gost hash: 940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81

and the output from above is : mypasswordforthatjob

time for stegnography: 
downloaded file name biner
and its password protect which is the above we found.

and we found a test file in which we got:
user: boring
password: iconvertedmypasswordtobinary //password was in binary format.




flag{9fdafbd64c47471a8f54cd3fc64cd312}





...............................................................
====================================================================
....................................................................

#1	What is the value of local_ch when its corresponding movl instruction is called (first if multiple)? 
	Ans: 1

#2	What is the value of eax when the imull instruction is called?
	Ans: 

#3	What is the value of local_4h before eax is set to 0?
	Ans: 

....................................................................
====================================================================