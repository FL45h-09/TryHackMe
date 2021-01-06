#Day-14
....................................................................
====================================================================
Day 14: Where's Rudolph?:

Twas the night before Christmas and Rudolph is lost
Now Santa must find him, no matter the cost
You have been hired to bring Rudolph back
How are your OSINT skills? Follow Rudolph's tracks...

====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------

#Task 1

While hunting and searching for any hints or clues
Santa uncovers some details and shares the news
Rudolph loved to use Reddit and browsed aplenty
His username was 'IGuidetheClaus2020'

so we have used the search ening called: https://namechk.com/ to find the differnt accounts with the given user id.

and we found the reddit account.

https://www.reddit.com/user/IGuidetheClaus2020/comments

this is the url.

then we scroll through the account and we found that Rudolph was born in chicago.

Rudolph's creator name is Robert May. we found that by just googling around.

then we found the another account on twitter.

the id on twitter is iGuideClaus2020

Ang scrolling through his twitter profile we fgound that he likes the Bechelorette show.

he took the part in parade and it was in chicago. adn we found that by a photo which was schared on his profile. we took that photo and image search it for the referance images to find the desired information.

there was an high quality copy of the image in his profile. so we downloaded that.

now its use the exif tool to extract the metadata from the image.

the photo was taken at 41.878113, -87.629799 this place.

and we got the flag in that metadata: {flag}ALWAYSCHECKTHEEXIFD4T4

he has been pawned and his password is: spygame and we found that using: https://scylla.sh

and the street no where he is right now is: 540. and we found that by googling those coordinates and zooming in in the map and looking for the hotel marriott.

...............................................................
====================================================================
....................................................................

#1	What URL will take me directly to Rudolph's Reddit comment history?
	Ans: https://www.reddit.com/user/IGuidetheClaus2020/comments

#2	According to Rudolph, where was he born?
	Ans: Chicago

#3	Rudolph mentions Robert.  Can you use Google to tell me Robert's last name?
	Ans: May

#4	On what other social media platform might Rudolph have an account?
	Ans: Twitter

#5	What is Rudolph's username on that platform?
	Ans: IGuideClaus2020

#6	What appears to be Rudolph's favorite TV show right now?
	Ans: Bachelorette

#7	Based on Rudolph's post history, he took part in a parade.  Where did the parade take place?
	Ans: chicago

#8	Okay, you found the city, but where specifically was one of the photos taken?
	Ans: 41.878113, -87.629799

#9	Did you find a flag too?
	Ans: {flag}ALWAYSCHECKTHEEXIFD4T4

#10	Has Rudolph been pwned? What password of his appeared in a breach?
	Ans: spygame

#11	Based on all the information gathered.  It's likely that Rudolph is in the Windy City and is staying in a hotel on Magnificent Mile.  What are the street numbers of the hotel address?
	Ans: 540

....................................................................
====================================================================