#Day-19
....................................................................
====================================================================
#Day 19	: Server-Side Request Forgery - Story:

Santa has released a web app that lets the children of the world check whether they are currently on the naughty or nice list. Unfortunately, the elf who coded it exposed more things than she thought. Can you access the list administration and ensure that every child gets a present from Santa this year?

Feel free to try hacking this web app on your own, or follow the instructions below! Note: when bypassing the hostname filter, use localtest.me otherwise your attempts won't work!

Can't bypass the naughty or nice list yourself? Watch the creator (@Tib3rius) solve today's challenge.!

====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------
when we search the name we get this kind of request in url
http://10.10.77.224/?proxy=
http://list.hohoho:8080/search.php?name=vishal

Be good for goodness sake! 

THM{EVERYONE_GETS_PRESENTS}


...............................................................
====================================================================
....................................................................

#1	What is Santa's password?
	Ans: Be good for goodness sake!

#2	What is the challenge flag?
	Ans: THM{EVERYONE_GETS_PRESENTS}

....................................................................
====================================================================