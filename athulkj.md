# Level 0-1

bandit0@bandit:~$ ls

readme

bandit0@bandit:~$ cat readme

boJ9jbbUNNfktd78OOpsqOltutMc3MY1

bandit0@bandit:~$ exit

# Level 1-2

bandit1@bandit:~$ ls

###### -

bandit1@bandit:~$ cat ./-

CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

bandit1@bandit:~$ exit

# Level 2-3

bandit2@bandit:~$ ls

spaces in this filename

bandit2@bandit:~$ cat spaces\ in\ this\ filename

UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

bandit2@bandit:~$ exit

# Level 3-4

bandit3@bandit:~$ cd inhere

bandit3@bandit:~/inhere$ ls

bandit3@bandit:~/inhere$ ls -a

.  ..  .hidden

bandit3@bandit:~/inhere$ cat .hidden

pIwrPrtPN36QITSp3EQaw936yaFoFgAB

bandit3@bandit:~/inhere$ exit

# Level 4-5

bandit4@bandit:~$ cd inhere

bandit4@bandit:~/inhere$ ls -a

.  ..  -file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09

bandit4@bandit:~/inhere$ file *

file: Cannot open `ile00' (No such file or directory).

file: Cannot open `ile01' (No such file or directory).

file: Cannot open `ile02' (No such file or directory).

file: Cannot open `ile03' (No such file or directory).

file: Cannot open `ile04' (No such file or directory).

file: Cannot open `ile05' (No such file or directory).

file: Cannot open `ile06' (No such file or directory).

file: Cannot open `ile07' (No such file or directory).

file: Cannot open `ile08' (No such file or directory).

file: Cannot open `ile09' (No such file or directory).

bandit4@bandit:~/inhere$ file inhere/*

inhere/*: cannot open `inhere/*' (No such file or directory)

bandit4@bandit:~/inhere$ file ./-*

./-file00: data

./-file01: data

./-file02: data

./-file03: data

./-file04: data

./-file05: data

./-file06: data

./-file07: ASCII text

./-file08: data

./-file09: data

bandit4@bandit:~/inhere$ cat ./-file07

koReBOKuIDDepwhWk7jZC0RTdopnAYKh

bandit4@bandit:~/inhere$ exit

# Level 5-6

bandit5@bandit:~$ cd inhere

bandit5@bandit:~/inhere$ ls -a

.   maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18

..  maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19

bandit5@bandit:~/inhere$ find -type f -size 1033c

./maybehere07/.file2

bandit5@bandit:~/inhere$ cat ./maybehere07/.file2

DXjZPULLxYr17uwoI01bNLQbtFemEgo7

# Level 6-7

bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c

find: ‘/root’: Permission denied

find: ‘/home/bandit28-git’: Permission denied

Find: ‘/home/bandit30-git’: Permission denied

find: ‘/home/bandit5/inhere’: Permission denied

find: ‘/home/bandit27-git’: Permission denied

find: ‘/home/bandit29-git’: Permission denied

find: ‘/home/bandit31-git’: Permission denied

find: ‘/lost+found’: Permission denied

find: ‘/etc/ssl/private’: Permission denied

find: ‘/etc/polkit-1/localauthority’: Permission denied

find: ‘/etc/lvm/archive’: Permission denied

find: ‘/etc/lvm/backup’: Permission denied

find: ‘/sys/fs/pstore’: Permission denied

find: ‘/proc/tty/driver’: Permission denied

find: ‘/proc/18015/task/18015/fd/6’: No such file or directory

find: ‘/proc/18015/task/18015/fdinfo/6’: No such file or directory

find: ‘/proc/18015/fd/5’: No such file or directory

find: ‘/proc/18015/fdinfo/5’: No such file or directory

find: ‘/cgroup2/csessions’: Permission denied

find: ‘/boot/lost+found’: Permission denied

find: ‘/tmp’: Permission denied

find: ‘/run/lvm’: Permission denied

find: ‘/run/screen/S-bandit14’: Permission denied

find: ‘/run/screen/S-bandit16’: Permission denied

find: ‘/run/screen/S-bandit22’: Permission denied

find: ‘/run/screen/S-bandit4’: Permission denied

find: ‘/run/screen/S-bandit31’: Permission denied

find: ‘/run/screen/S-bandit24’: Permission denied

find: ‘/run/screen/S-bandit21’: Permission denied

find: ‘/run/screen/S-bandit0’: Permission denied

find: ‘/run/screen/S-bandit25’: Permission denied

find: ‘/run/screen/S-bandit23’: Permission denied

find: ‘/run/screen/S-bandit20’: Permission denied

find: ‘/run/shm’: Permission denied

find: ‘/run/lock/lvm’: Permission denied

find: ‘/var/spool/bandit24’: Permission denied

find: ‘/var/spool/cron/crontabs’: Permission denied

find: ‘/var/spool/rsyslog’: Permission denied

find: ‘/var/tmp’: Permission denied

find: ‘/var/lib/apt/lists/partial’: Permission denied

find: ‘/var/lib/polkit-1’: Permission denied

/var/lib/dpkg/info/bandit7.password

find: ‘/var/log’: Permission denied

find: ‘/var/cache/apt/archives/partial’: Permission denied

find: ‘/var/cache/ldconfig’: Permission denied

bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password

HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

bandit6@bandit:~$ exit

# Level 7-8

bandit7@bandit:~$ ls

data.txt

bandit7@bandit:~$ grep 'millionth' data.txt

millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV

bandit7@bandit:~$ exit

# Level 8-9

bandit8@bandit:~$ sort data.txt | uniq -u

UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

bandit8@bandit:~$ exit

# Level 9-10

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

&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

S=A.H&^

bandit9@bandit:~$ exit










