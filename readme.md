lvl 0
ssh bandit0@bandit.labs.overthewire.org -p 2220
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
cat is used for reading
I learnt the following things from this level:
Use of cat and ls


lvl 1-lvl2
ssh bandit1@bandit.labs.overthewire.org -p 2220
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
I leant the following from this level
naming - file names


lvl2-lvl3
ssh bandit2@bandit.labs.overthewire.org -p 2220
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
I learnt 
calling files withs spaces


lvl3-lvl4
ssh bandit3@bandit.labs.overthewire.org -p 2220
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
I learnt 
using -a to see hidden file
periods used to make file hidden


lvl4-lvl5
ssh bandit4@bandit.labs.overthewire.org -p 2220
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
ls
cat inhere
ls
file ./-*
cat ./-file07



lvl5-lvl6
ssh bandit5@bandit.labs.overthewire.org -p 2220
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
ls
cd inhere
ls 
ls -a
find -size 1033c
cd maybehere07
cat .file2


lvl6-lvl7
ssh bandit6@bandit.labs.overthewire.org -p 2220
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
find -type f
ls
cat ./.
find / -user bandit7
cat /var/lib/dpkg/info/bandit7.password
Things learnt 
can also use
find / -user bandit7 -group bandit6

lvl7-lvl8
ssh bandit7@bandit.labs.overthewire.org -p 2220
cvX2JJa4CFALtqS87jk27qwqGhBM9plV
ls
ls -a
grep millionth data.txt
Things learnt 
sometimes not posssible to check solution applying only one filter and then manually like in lvl6 if file is large
sort cannot be used in this lvl


lvl8-lvl9
ssh bandit8@bandit.labs.overthewire.org -p 2220
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
sort data.txt | uniq -u
Things learnt
grepping


lvl9-lvl10
ssh bandit9@bandit.labs.overthewire.org -p 2220
truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
strings data.txt|grep '='
