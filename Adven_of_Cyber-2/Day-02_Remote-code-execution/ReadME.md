#Day-2
===================================================================
After your heroic deeds regaining control of the control centre yesterday, Elf McSkidy has decided to give you an important job to do.

"We know we've been hacked, so we need a way to protect ourselves! The dev team have set up a website for the elves to upload pictures of any suspicious people hanging around the factory, but we need to make sure it's secure before we add it to the public network. Please perform a security audit on the new server and make sure it's unhackable!"
===================================================================

*/

php Revershell script can be found:
/usr/share/webshells/php/php-reverse-shell.php

/*

Id given by them: ODIzODI5MTNiYmYw

to reach to the upload section we need to do following:
http://10.10.245.64/index.php?id=ODIzODI5MTNiYmYw

#1	What string of text needs adding to the URL to get access to the upload page?
	Ans: ?id=ODIzODI5MTNiYmYw

#2	What type of file is accepted by the site?
	Ans: Image

Bypass the filter and upload a reverse shell.
we can do that by renaming our reverse shell php file like below:
#php-reverse-shell.jpeg.php

#3	In which directory are the uploaded files stored?
	Ans: we can use gobuster to find but lets just try some common: /uploads/

#4	Activate your reverse shell and catch it in a netcat listener!
	just upload your converted php script through that upload form and navigate to that file location such as:
	http://10.10.245.64/uploads/shell.jpg.php

#5	