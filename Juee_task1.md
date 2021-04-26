saee@DESKTOP-NB456GS ~

LEVEL 0

$ ssh bandit0@bandit.labs.overthewire.org -p 2220
Then it asks to type yes if its the first time and then asks to type the password that is bandit0.

bandit0@bandit.labs.overthewire.org's password:

bandit0@bandit:~$ ls -alps
It shows all the files. Then we have to get the password from readme file.

bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1

bandit0@bandit:~$ exit
Then we exit from level zero and go to level 1

LEVEL 1

$ ssh bandit1@bandit.labs.overthewire.org -p 2220
bandit1@bandit.labs.overthewire.org's password:

Enter the password we got.

bandit1@bandit:~$ ls -alps

This again shows us the directories and we need to get the password from a file.

bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit1@bandit:~$ exit
Then we exit from level 1 and go to level 2

LEVEL 2

$  ssh bandit2@bandit.labs.overthewire.org -p 2220
bandit2@bandit.labs.overthewire.org's password:
bandit2@bandit:~$ ls -alps

Now there are spaces in the file name so to indicate that use backslash.

bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
bandit2@bandit:~$ exit

LEVEL 3

$  ssh bandit3@bandit.labs.overthewire.org -p 2220
bandit3@bandit.labs.overthewire.org's password:

bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls -al

Then we see the hidden file.

bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
bandit3@bandit:~/inhere$ exit

LEVEL 4

$  ssh bandit4@bandit.labs.overthewire.org -p 2220
bandit4@bandit.labs.overthewire.org's password:

bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls

It shows all the files.Tried all files till got a password.

bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
bandit4@bandit:~/inhere$ exit

LEVEL 5

$  ssh bandit5@bandit.labs.overthewire.org -p 2220
bandit5@bandit.labs.overthewire.org's password:

bandit5@bandit:~$ find . -type f -readable ! -executable -size 1033c
./inhere/maybehere07/.file2
bandit5@bandit:~$ cat ./inhere/maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7

We find the suitable file and get the password.

                                                                                                          bandit5@bandit:~$ exit
                                                                                                        LEVEL 6
                                                                                                        $  ssh bandit6@bandit.labs.overthewire.org -p 2220
bandit6@bandit.labs.overthewire.org's password:

bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c

Then got a lot of files with permission denied. But in the big list, a I saw a file manually which should have the password and then opened the file.

bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
bandit6@bandit:~$ exit

LEVEL 7

$  ssh bandit7@bandit.labs.overthewire.org -p 2220
bandit7@bandit.labs.overthewire.org's password:

grep enables us to search through text files.

bandit7@bandit:~$ grep "millionth" data.txt
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV
bandit7@bandit:~$ exit

LEVEL 8

$  ssh bandit8@bandit.labs.overthewire.org -p 2220
bandit8@bandit.labs.overthewire.org's password:

We first sort the data so that it comes adjacent. And then we can use uniq command. 

bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
bandit8@bandit:~$ exit

LEVEL 9

$  ssh bandit9@bandit.labs.overthewire.org -p 2220
bandit9@bandit.labs.overthewire.org's password:

Now we know that the password is preceeded by several == characters... so we can increase the number of = in each grep search to get the password

bandit9@bandit:~$ strings data.txt | grep =
========== the*2i"4
=:G e
========== password
<I=zsGi
Z)========== is
A=|t&E
Zdb=
c^ LAh=3G
*SF=s
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
S=A.H&^
bandit9@bandit:~$ strings data.txt | grep ==
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

So here we got the password in the last line

bandit9@bandit:~$ exit

LEVEL 10

$  ssh bandit10@bandit.labs.overthewire.org -p 2220
bandit10@bandit.labs.overthewire.org's password:

The password is encoded in base 64. So that command will help it to get decoded.

bandit10@bandit:~$ base64 -d data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
bandit10@bandit:~$ exit



                                                                                            


