export ip=10.10.210.54


task 1:
=================================
Let's go ahead and start with the basics and perform a syn scan on the box provided. What will this command be without the host IP address?

Answer: nmap -sS

==================

task 2:
------------------------------------
After scanning this, how many ports do we find open under 1000?

Ans: 2 ports, 22 & 80  | nmap -sS $ip

==========================

task 3:
-------------------------------------
What communication protocol is given for these ports following the port number?

Ans: tcp.

=======================

task 4:
--------------------------------------
 Perform a service version detection scan, what is the version of the software running on port 22?

 Ans: 6.6.1p1 | nmap -sV -p 22 $ip

=======================================

task 5:
------------------------------------
Perform an aggressive scan, what flag isn't set under the results for port 80?

Ans: httponly | nmap -A -v $ip

===============================

task 6:
-----------------------------------
Perform a script scan of vulnerabilities associated with this box, what denial of service (DOS) attack is this box susceptible to? Answer with the name for the vulnerability that is given as the section title in the scan output. A vuln scan can take a while to complete. In case you get stuck, the answer for this question has been provided in the hint, however, it's good to still run this scan and get used to using it as it can be invaluable. 

Ans: http-slowloris-check | nmap --script vuln $ip

===========================================