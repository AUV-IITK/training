LEVEL 0: ssh bandit0@bandit.labs.overthewire.org -p 2220 pass:bandit0 ls
cat readme LEVEL 1: ssh bandit1@bandit.labs.overthewire.org -p 2220
pass:boJ9jbbUNNfktd78OOpsqOltutMc3MY1 ls cat ./- LEVEL 2: ssh
bandit2@bandit.labs.overthewire.org -p 2220
pass:CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9 ls cat "spaces in this filename"
LEVEL 3: ssh bandit3@bandit.labs.overthewire.org -p 2220
pass:UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK ls cd inhere ls -A cat '.hidden'
LEVEL 4: ssh bandit4@bandit.labs.overthewire.org -p 2220
pass:pIwrPrtPN36QITSp3EQaw936yaFoFgAB ls cd inhere ls find ./\* cat
./-file07\
LEVEL 5: ssh bandit5@bandit.labs.overthewire.org -p 2220
pass:koReBOKuIDDepwhWk7jZC0RTdopnAYKh ls cd inhere ls find ./\* -size
1033c ! -executable cat ./maybehere07/.file2 LEVEL 6: ssh
bandit6@bandit.labs.overthewire.org -p 2220
pass:DXjZPULLxYr17uwoI01bNLQbtFemEgo7 ls cd / ls find / -group bandit6
-user bandit7 -size 33c cat /var/lib/dpkg/info/bandit7.password LEVEL 7:
ssh bandit7@bandit.labs.overthewire.org -p 2220
pass:HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs ls cat data.txt ctrl+c cat
\~/data.txt | grep millionth LEVEL 8: ssh
bandit8@bandit.labs.overthewire.org -p 2220
pass:cvX2JJa4CFALtqS87jk27qwqGhBM9plV ls sort data.txt | uniq sort
data.txt | uniq -u LEVEL 9: ssh bandit9@bandit.labs.overthewire.org -p
2220 pass:UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR ls strings data.txt strings
data.txt | grep = LEVEL 10: ssh bandit10@bandit.labs.overthewire.org -p
2220 pass:truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
