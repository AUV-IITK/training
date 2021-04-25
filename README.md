# training
For AUV Training 2021
#level0
ssh bandit0@bandit.labs.overthewire.org -p 2220
bandit0@bandit.labs.overthewire.org's password:bandit0 
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1 ~password for level1
bandit0@bandit:~$ exit 

#level1
ssh bandit1@bandit.labs.overthewire.org -p 2220
bandit0@bandit.labs.overthewire.org's password:boJ9jbbUNNfktd78OOpsqOltutMc3MY1
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9 ~passord for level2
bandit1@bandit:~$ exit 

#level2
ssh bandit2@bandit.labs.overthewire.org -p 2220
bandit2@bandit.labs.overthewire.org's password:CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat spaces\ in\ this\ filename
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK ~password for level3
bandit2@bandit:~$ exit 

#level3
ssh bandit3@bandit.labs.overthewire.org -p 2220
bandit3@bandit.labs.overthewire.org's password:UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls -al
total 12
drwxr-xr-x 2 root    root    4096 May  7  2020 .
drwxr-xr-x 3 root    root    4096 May  7  2020 ..
-rw-r----- 1 bandit4 bandit3   33 May  7  2020 .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB ~password for level4
bandit3@bandit:~$ exit 

#level4
ssh bandit4@bandit.labs.overthewire.org -p 2220
bandit4@bandit.labs.overthewire.org's password:pIwrPrtPN36QITSp3EQaw936yaFoFgAB
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls -all
bandit4@bandit:~/inhere$ find . -type f | xargs file
-file07 is the only one with ASCII code
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh ~password for level5
bandit4@bandit:~$ exit

#level5
ssh bandit5@bandit.labs.overthewire.org -p 2220
bandit5@bandit.labs.overthewire.org's password:koReBOKuIDDepwhWk7jZC0RTdopnAYKh
bandit5@bandit:~/inhere$ find . -type f -size 1033c ! -executable
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7 ~password for level6
bandit5@bandit:~$ exit

 #level6
ssh bandit6@bandit.labs.overthewire.org -p 2220
bandit6@bandit.labs.overthewire.org's password:DXjZPULLxYr17uwoI01bNLQbtFemEgo7
bandit6@bandit:~$ find / -type f -size 33c -user bandit7 -group bandit6
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs ~password for level7
bandit6@bandit:~$ exit
 
#level7
ssh bandit7@bandit.labs.overthewire.org -p 2220
bandit7@bandit.labs.overthewire.org's password:HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
bandit7@bandit:~$ ls
data.txt
bandit7@bandit:~$ cat data.txt | grep millionth
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV ~password for level8
bandit7@bandit:~$ exit

#level8
ssh bandit8@bandit.labs.overthewire.org -p 2220
bandit8@bandit.labs.overthewire.org's password:cvX2JJa4CFALtqS87jk27qwqGhBM9plV
bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR ~password for level9
bandit7@bandit:~$ exit

#level9
ssh bandit9@bandit.labs.overthewire.org -p 2220
bandit9@bandit.labs.overthewire.org's password:UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
bandit9@bandit:~$ strings data.txt | grep '='
========== the*2i"4
=:G e
========== password
<I=zsGi
Z)========== is
A=|t&E
Zdb=
c^ LAh=3G
*SF=s
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk ~password for level10
bandit7@bandit:~$ exit

#level10
ssh bandit10@bandit.labs.overthewire.org -p 2220
bandit10@bandit.labs.overthewire.org's password:truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
bandit10@bandit:~$ base64 --decode data.txt
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
