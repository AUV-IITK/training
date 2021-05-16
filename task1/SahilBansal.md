# ASSIGNMENT-1

## overthewire- BANDIT wargame level1-10

#### Level-0
**ssh bandit0@bandit.labs.overthewire.org -p 2220**

#### Level-1
**cat readme**- it printed the contents of readme file(the password) on the terminal.

#### Level-2
**cat ./-**

#### Level-3
**cat spa\***- use of wildcards.

#### Level-4
**cd inhere**>>
**ls -a**- to get the file name *.hidden*>>
**cat .hidden**

#### Level-5
**cd inhere**>>
**ls -a**>>
**file ./-file\***- to get the type of each file. *-file07* was ascii text and hence human readable.>>>
**cat ./-file07**

#### Level-6
**cd inhere**>>
**ls -a**>>
**find m\* -size 1033c**- ouputs the file(*maybehere07/.file2*) whose size is 1033 bytes.>>
**cat maybehere07/.file2**

#### level-7
**find / -size 33c -user bandit7 -group bandit6** - for most of the files permission was denied, I have permission to read only one file */var/lib/dpkg/info/bandit7.password* so i looked in it to get the password.

#### Level-8
**grep "millionth" data.txt**

#### Level-9
**sort data.txt | uniq -u**- the sort commands sorted the file data.txt so that similar strings were now one after the another, the the uniq command does its job, the -u option prints only unique lines which here gives the password.

#### level-10
**strings data.txt | grep "====="**- the strings command gives only the readable text from a binary file.

#### Level-11
**base64 data.txt -d**- this command decodes the data from base64 system.

#### Level-12
**cat data.txt | tr ‘n-za-mN-ZA-M’ ‘a-zA-Z’** password to bandit12-  5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu.