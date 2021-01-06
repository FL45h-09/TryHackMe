#Day-16
....................................................................
====================================================================
#Day 16: Find Santa
 Oh no! Santa 🎅 has taken off, leaving you -- the faithful elves behind! Can you help find Santa's location?

Luckily, the elves are OSINT masters and remember a thing or two. Specifically, they remember:

    Santa has a webpage at 10.10.69.122/static/index.html to help lost elves find their way home. Santa never told the elves what port number the webserver is on. Can you find out?!
    This webpage has a link somewhere on it, hidden away so anyone that isn't an elf can't find it.
    Santa's Sled has an API we can talk too. The key for the API is between 0 and 100, and it's an odd number. But be careful! After an unknown number of attempts, Santa's Sled will ban your IP address. 

Deploy the machine that is running Santa's Sled and allow a couple of minutes for the target (10.10.69.122) to start up. Using your Python skills from Day 15 to find the correct key for the API.
====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------
Running the nmap to start the basic enumeration on the given target ip.

#nmap -A -sC -sV -O -oN initial 10.10.69.122

so we found that the web srver is running on the port 8000.

now lets find the api derectory by using python script

we have named the script as test.py

and by the we found the api dercotory.

/api/api_key


so now lets try to brute force the api for odd numbers from 0 100 by creating another python script.
we have stored it as odd.py

and by burteforcing the api we found the api umber is 57

and santa is at: Winter Wonderland, Hyde Park, London

...............................................................
====================================================================
....................................................................

#1	What is the port number for the web server?
	Ans: 8000

#2	Without using enumerations tools such as Dirbuster, what is the directory for the API?  (without the API key)
	Ans: /api/

#3	Where is Santa right now?
	Ans: Winter Wonderland, Hyde Park, London

#4	Find out the correct API key. Remember, this is an odd number between 0-100. After too many attempts, Santa's Sled will block you. To unblock yourself, simply terminate and re-deploy the target instance (10.10.69.122)
	Ans: 57

....................................................................
====================================================================