#Day-4
====================================================================
We're going to be taking a look at some of the fundamental tools used in web application testing. You're going to learn how to use Gobuster to enumerate a web server for hidden files and folders to aid in the recovery of Elf's forums. Later on, you're going to be introduced to an important technique that is fuzzing, where you will have the opportunity to put theory into practice.

Our malicious, despicable, vile, cruel, contemptuous, evil hacker has defaced Elf's forums and completely removed the login page! However, we may still have access to the API. The sysadmin also told us that the API creates logs using dates with a format of YYYYMMDD.
====================================================================


we 1st useed gobuster to find the api directory.
Command as below:
#gobuster dir -u $IP -w /usr/share/dirb/wordlists/common.txt | tee -a gobuster

=
--------------------------------------------------------------------

And then later we used wfuzz to fuzz the api file with given wordlist for date parameter.
command as below:
#fuzz -c -z file,wordlist http://10.10.222.103/api/site-log.php?date=FUZZ | tee -a wfuzz

=
-------------------------------------------------------------------