#Documentation for Web Fundamentals(ctf)

#Title THM Web MiniCTF.


===================================================================

#get request: curl http://10.10.124.211:8081/ctf/get
*/
For simple get request we dont nee to ad any parameters or options in curl command.
/*

------------------------------------------------------------------

#post request: curl -X POST -d "flag_please" http://10.10.124.211:8081/ctf/post

*/
-X is the method to use(here its post methid.). and -d is to send the data to server(here its "flag_please").
/*

------------------------------------------------------------------

#getcookie from server: curl -c ./coockie.txt http://10.10.124.211:8081/ctf/getcookie

*/
-c is to collect cookie from server. here we are collection cookie from server on our local machine in this case /root/Documents/TryHackMe/webfundamentals/cookie
/*

------------------------------------------------------------------

#sendcookie to server: curl -b ./coockie_set http://10.10.124.211:8081/ctf/sendcookie

*/
-b is to send the desire cookie to server. to sent the cookie to server we need to create a cookie on our local machine and then spcify the path and url of the server in curl command.
/root/Documents/TryHackMe/webfundamentals/cookie_set
/*

===================================================================