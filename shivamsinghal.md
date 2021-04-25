# OVER THE WIRE
## SHIVAM SINGHAL

### Level 0
~~~
ssh bandit0@bandit.labs.overthewire.org -p 2220
~~~
enter the password: bandit0

Login complete

**commands learnt: ssh**
***

### Level 0->Level 1
~~~
ls
file readme
cat readme      //returns the password
exit
ssh bandit1@bandit.labs.overthewire.org -p 2220
~~~
enter the password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

Login complete

**commands learnt: ls,file,cat**

***
### Level 1->Level 2

~~~
ls
cat ./-       // ./ used to read a dashed file
exit
ssh bandit2@bandit.labs.overthewire.org -p 2220
~~~
enter the password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

Login complete

**commands learnt: How to read dashed file**
***
### Level 2->Level 3

~~~
ls
cat spaces\ in\ this\ filename
exit
ssh bandit3@bandit.labs.overthewire.org -p 2220
~~~
enter the password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

Login complete

**commands learnt: How to read spaces in file name using skip character**
***
### Level 3->Level 4

~~~
ls
cd inhere
find
cat ./.hidden
exit
ssh bandit4@bandit.labs.overthewire.org -p 2220
~~~
enter the password: pIwrPrtPN36QITSp3EQaw936yaFoFgAB

Login complete

**commands learnt: cd, find and read hidden files**
***
### Level 4->Level 5

~~~
ls
cd inhere
find
file ./-file0*
cat ./-file07
exit
ssh bandit5@bandit.labs.overthewire.org -p 2220
~~~
enter the password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

Login complete

**commands learnt: use file to check the file type and read the desired file**
***
### Level 5->Level 6

~~~
ls
cd inhere
find . -size 1033c
cat ./maybehere07/.file2
exit
ssh bandit6@bandit.labs.overthewire.org -p 2220
~~~
enter the password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

Login complete

**commands learnt: find a file of a particular size and use its address with cat command to read**
***
### Level 6->Level 7

~~~
find /var -user bandit7
cat /var/lib/dpkg/info/bandit7.password
exit
ssh bandit7@bandit.labs.overthewire.org -p 2220
~~~
enter the password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

Login complete

**commands learnt: read the file owned by a user**
***
### Level 7->Level 8

~~~
ls
grep -w "millionth" data.txt
exit
ssh bandit8@bandit.labs.overthewire.org -p 2220
~~~
enter the password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

Login complete

**commands learnt: grep**
***
### Level 8->Level 9

~~~
cat data.txt | sort | uniq -u
exit
ssh bandit9@bandit.labs.overthewire.org -p 2220
~~~
enter the password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

Login complete

**commands learnt: sort, uniq, multiple commands at same time**
***
### Level 9->Level 10

~~~
strings data.txt | grep "="
exit
ssh bandit10@bandit.labs.overthewire.org -p 2220
~~~
enter the password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

Login complete

**commands learnt: uses of grep**
***

### Level 10->Level 11

~~~
base64 -d data.txt
exit
ssh bandit11@bandit.labs.overthewire.org -p 2220
~~~
enter the password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

Login complete

**commands learnt: base64,-d(decode) to convert given data to decimal representation**

***
### Level 11->Level 12

~~~
cat data.txt
cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
exit
ssh bandit12@bandit.labs.overthewire.org -p 2220
~~~
enter the password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

Login complete

**commands learnt: tr and using multiple commands at same time**

***
### Level 12->Level 13

~~~
mkdir /tmp/findpass
cp data.txt /tmp/findpass
cd /tmp/findpass
file data.txt
cat data.txt | xxd -r
cat data.txt | xxd -r> data
file data
mv data data2.gz
gzip -d data2.gz
ls
file data2
mv data2 data3.bz2
bzip2 -d data3.bz2
ls
file data3
mv data3 data4.gz
gzip -d data4.gz
ls
file data4
mv data4 data5.tar
tar -xf data5.tar
ls
file data5.bin
mv data5.bin data6.tar
tar -xf data6.tar
ls
file data6.bin
mv data6.bin data7.bz2
bzip2 -d data7.bz2
ls
file data7
mv data7 data8.tar
tar -xf data8.tar
ls
file data8.bin
mv data8.bin data9.gz
gzip -d data9.gz
ls
file data9
data9: ASCII text
bandit12@bandit:/tmp/findpass$ cat data9

exit
ssh bandit13@bandit.labs.overthewire.org -p 2220
~~~
enter the password: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

Login complete

**commands learnt: various types of compressed files, how to decompress them, creating a temp file, saving a file with different extension**
