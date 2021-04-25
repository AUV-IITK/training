Submit your files in this folder. 
level 0
ssh bandit0@bandit.labs.overthewire.org -p 2220
yes
bandit0

level 1
ls
cat readme
exit
ssh bandit1@bandit.labs.overthewire.org -p 2220

level 2
ls
cat ./-
exit
ssh bandit2@bandit.labs.overthewire.org -p 2220

level 3
ls
cat "spaces in this filename"
exit
ssh bandit3@bandit.labs.overthewire.org -p 2220

level 4
ls
cd inhere
ls -a
cat .hidden 
exit
ssh bandit4@bandit.labs.overthewire.org -p 2220

level 5
ls -a
cd inhere
ls -a
cat ./-file07 (tried out all files:|, then got to know file ./-* )
exit
ssh bandit5@bandit.labs.overthewire.org -p 2220

level 6
ls -a
cd inhere
ls -a
du -alh ( didnt help. no file with size around 1k, so tried next)
find -size 1033c ( the same file in above command showed 4k size, i dont know why)
exit
ssh bandit6@bandit.labs.overthewire.org -p 2220

level 7
find / -user bandit7 -group bandit6 -size 33c
found this only file where permission was not denied
cat /var/lib/dpkg/info/bandit7.password
exit
ssh bandit7@bandit.labs.overthewire.org -p 2220

level 8
ls -a
grep millionth data.txt
exit
ssh bandit8@bandit.labs.overthewire.org -p 2220

level 9
ls 
sort data.txt | uniq -c | sort -nr
exit
ssh bandit9@bandit.labs.overthewire.org -p 2220

level 10
ls
strings data.txt | grep "="
exit
ssh bandit10@bandit.labs.overthewire.org -p 2220

level 11
ls
base64 -d data.txt
exit
ssh bandit11@bandit.labs.overthewire.org -p 2220








