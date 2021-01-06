#Day-7
....................................................................
====================================================================
It's 6 AM and Elf McSkidy is clocking-in to The Best Festival Company's SOC headquarters to begin his watch over TBFC's infrastructure. After logging in, Elf McEager proceeds to read through emails left by Elf McSkidy during the nightshift.

More automatic scanning alerts, oh look, another APT group. It feels like it's going to be a long, but easy start to the week for Elf McEager.

Whilst clearing the backlog of emails, Elf McEager reads the following: "URGENT: Data exfiltration detected on TBFC-WEB-01". "Uh oh" goes Elf McEager. "TBFC-WEB-01? That's Santa's webserver! Who has the motive to steal data from there?!". It's time for the ever-vigilant Elf McEager to prove his salt and find out exactly what happened.

Unknowingly to Elf McEager, Elf McSkidy made this all up! Fortunately, this isn't a real attack - but a training exercise created ahead of Elf McEager's performance review.
====================================================================
....................................................................

#1	Open "pcap1.pcap" in Wireshark. What is the IP address that initiates an ICMP/ping?
	Ans: 10.11.3.2

#2	If we only wanted to see HTTP GET requests in our "pcap1.pcap" file, what filter would we use?
	Ans: http.request.method == get

#3	Now apply this filter to "pcap1.pcap" in Wireshark, what is the name of the article that the IP address "10.10.67.199" visited?
	Ans: reindeer-of-the-week
	this is was under the /post.

#4	Let's begin analysing "pcap2.pcap". Look at the captured FTP traffic; what password was leaked during the login process? There's a lot of irrelevant data here - Using a filter here would be useful!
	Ans: plaintext_password_fiasco
	We descover this by using follow stream option by right clicking on it.

#5	Continuing with our analysis of "pcap2.pcap", what is the name of the protocol that is encrypted?
	Ans: ssh

#6	Analyse "pcap3.pcap" and recover Christmas! What is on Elf McSkidy's wishlist that will be used to replace Elf McEager?
	Ans: Rubber Ducky
	we can follow the stream to check whats inside and once we found the christmas.zip then we export the http. then we extract the zip and found the answer.