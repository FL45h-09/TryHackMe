#Day-6

--
====================================================================
#This year, 
Santa wanted to go fully digital and invented a "Make a wish!" system. It's an extremely simple web app that would allow people to anonymously share their wishes with others. Unfortunately, right after the hacker attack, the security team has discovered that someone has compromised the "Make a wish!". Most of the wishes have disappeared and the website is now redirecting to a malicious website.  An attacker might have pretended to submit a wish and put a malicious request on the server! The security team has pulled a back-up server for you on 10.10.214.107:5000. Your goal is to find the way the attacker could have exploited the application.
====================================================================

#1	What vulnerability type was used to exploit the application?
	Ans: stored cross-site scripting

#2	What query string can be abused to craft a reflected XSS?
	Ans: q

#3	Launch the OWASP ZAP Application.
	Ans: No Answer needed.

#4	Run a ZAP (zaproxy) automated scan on the target. How many XSS alerts are in the scan?
	Ans: 2

#5	Explore the XSS alerts that ZAP has identified, are you able to make an alert appear on the "Make a wish" website?
	Ans: No Answer needed.

