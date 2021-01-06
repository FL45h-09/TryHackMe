#Day-20
....................................................................
====================================================================
#Day 20	: PowershELlF to the rescue - Story:

Someone is mischievous at The Best Festival Company. The contents within the stockings have been removed. A clue was left in one of the stockings that hints that the contents have been hidden within Elfstation1. McEager moves quickly and attempts to RDP into the machine. Yikes! He is unable to log in.

Luckily, he has been learning PowerShell, and he can remote into the workstation using PowerShell over SSH.

Task: Use the PowerShell console to navigate throughout the endpoint to find the hidden contents to reveal what was hidden in the stockings.

====================================================================
....................................................................
#Steps I aquire to gain acccess:
----------------------------------
SSh in to powershell over ssh.

#Set-Location \Documents\

to list the hidden files we use cmdlet:
#get-childitem -hidden

to show the conntent we use"

#get-content -path filename.txt

now need to search the desktop for the hidden folder:

#get-childitem -hidden

now need to search the Windows directory for the specific folder

#get-childitem -recurs -hidden -ErrorAction SilentlyContinue

we found the folder there. Now we need to cound the words in 1st file.

#get-content -Path 1.txt | measure-Object -Word

Next up we have to find the specific words on the index of 551 and 6991:

#(get-content -Path 1.txt)[551]
#(get-content -Path 1.txt)[6991]

so we found the 2 words now need to find those Phrase in the 2nd file:

#Select-String -Path 2.txt -Pattern 'redryder'

And we found our last answer.

...............................................................
====================================================================
....................................................................

#1	Search for the first hidden elf file within the Documents folder. Read the contents of this file. What does Elf 1 want?
	Ans: 2 front teeth

#2	Search on the desktop for a hidden folder that contains the file for Elf 2. Read the contents of this file. What is the name of that movie that Elf 2 wants?
	Ans: Scorooged

#3	Search the Windows directory for a hidden folder that contains files for Elf 3. What is the name of the hidden folder? (This command will take a while)
	Ans: 3lfthr3e

#4	How many words does the first file contain?
	Ans: 9999

#5	What 2 words are at index 551 and 6991 in the first file?
	Ans: Red Ryder

#6	This is only half the answer. Search in the 2nd file for the phrase from the previous question to get the full answer. What does Elf 3 want? (use spaces when submitting the answer)
	Ans: Red Ryder BB Gun

....................................................................
====================================================================