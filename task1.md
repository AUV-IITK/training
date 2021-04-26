# level 0 

ssh bandit0@bandit.labs.overthewire.org -p2220


# level 1

bandit0@bandit:\~$ ls
readme
bandit0@bandit:\~$ cat readme

boJ9jbbUNNfktd78OOpsqOltutMc3MY1
 
  
# level 2

bandit1@bandit:\~$ cat ./-

CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9


# level 3

bandit2@bandit:\~$ cat spaces\ in\ this\ filename

UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK


# level 4

bandit3@bandit:\~$ cd inhere

bandit3@bandit:\~/inhere$ ls -a

.  ..  .hidden

bandit3@bandit:~/inhere$ cat .hidden

pIwrPrtPN36QITSp3EQaw936yaFoFgAB


# level 5

bandit4@bandit:\~/inhere$ file ./-file07

./-file07: ASCII text

bandit4@bandit:~/inhere$ cat ./-file07

koReBOKuIDDepwhWk7jZC0RTdopnAYKh


# level 6

bandit5@bandit:\~/inhere$ find . -size 1033c

./maybehere07/.file2

bandit5@bandit:~/inhere$ cat ./maybehere07/.file2

DXjZPULLxYr17uwoI01bNLQbtFemEgo7


# level 7

bandit6@bandit:\~$ find / -type f -size 33c -user bandit7 -group bandit6

/var/lib/dpkg/info/bandit7.password

bandit6@bandit:\~$ cat /var/lib/dpkg/info/bandit7.password

HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs


# level 8

bandit7@bandit:\~$ grep 'millionth' data.txt

millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV


# level 9

bandit8@bandit:\~$ sort data.txt

UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR //only line which occured only once


# level 10

bandit9@bandit:\~$ strings data.txt

truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk //preceded by several = 



# level 11

bandit10@bandit:\~$ bandit10@bandit:~$ base64 -d data.txt

The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
