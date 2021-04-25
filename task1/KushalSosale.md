SSH Assignment-1<br>
**Level 0**<br>
~ssh bandit0@bandit.labs.overthewire.org -p 2220<br>
~cat readme<br>
***Learnt cat command***<br>
-----------------
**Level 1**<br>
~ssh bandit1@bandit.labs.overthewire.org -p 2220<br>
~cat ./-<br>
***Learnt to read data from conflicting filenames***<br>
-------------------
**Level 2**<br>
~ssh bandit2@bandit.labs.overthewire.org -p 2220<br>
~cat 'spaces in this filename'<br>
---------------------
**Level 3**<br>
~ssh bandit3@bandit.labs.overthewire.org -p 2220<br>
~ls<br>
~cd inhere<br>
~find<br>
~cat ./.hidden<br>
***Learnt to read data from hidden files***<br>
------------------
**Level 4**   
~ssh bandit4@bandit.labs.overthewire.org -p 2220<br>
~ls<br>
~cd inhere<br>
~ls<br>
~file ./-file*<br>
~cat ./-file07<br>
***Learnt to search for files with human readable data***<br>
-----------------
**Level 5**<br>
~ssh bandit5@bandit.labs.overthewire.org -p 2220<br>
~ls<br>
~cd inhere<br>
~ls<br>
~find -type f -size 1033c ! -executable<br>
~cd maybehere07<br>
~cat ./.file2<br>
***Learnt to search for files with a particular size***<br>
------------------
**Level 6**<br>
~ssh bandit6@bandit.labs.overthewire.org -p 2220<br>
~find / -user bandit7 -group bandit6 -size 33c 2>/dev/null<br>
~cat /var/lib/dpkg/info/bandit7.password<br>
***Learnt to search for files used and grouped by different users***<br>
-------------------
**Level 7**<br>
~ssh bandit7@bandit.labs.overthewire.org -p 2220<br>
~ls<br>
~cat data.txt | grep millionth<br>
***Learnt to search for text adjacent to a particular word***<br>
---------------
**Level 8**<br>
~ssh bandit8@bandit.labs.overthewire.org -p 2220<br>
~ls<br>
~sort data.txt | uniq -u<br>
***Learnt to search for unique data in file***<br>
--------------
**Level 9**<br>
~ssh bandit9@bandit.labs.overthewire.org -p 2220<br>
~cat data.txt | strings<br>
~cat data.txt | strings | grep =<br>
-----------
**Level 10**<br>
~ssh bandit10@bandit.labs.overthewire.org -p 2220<br>
~cat data.txt | base64<br>
~cat data.txt | base64 --decode<br>
***Learnt to decode encoded data from txt file***<br>
----------
**Level 11**
~ssh bandit11@bandit.labs.overthewire.org -p 2220<br>
~ls<br>
~cat data.txt | strings<br>
~cat data.txt | tr "[n-za-mN-ZA-M]" "[a-zA-Z]"<br>
***Learnt how to use 'tr' command and how to decode ROT cyphers***<br>
------------
**Level 12**<br>
~mkdir /tmp/darkstar48<br>
~cp data.txt /tmp/darkstar48<br>
~cd /tmp/darkstar48<br>
~file data.txt<br>
~xxd -r data.txt > data<br>
~file data<br>
~mv data data.gz<br>
~gunzip data.gz<br>
~file data<br>
~mv data data.bz2<br>
~bzip2 -d data.bz2<br>
~ls<br>
~file data<br>
~mv data data.gz<br>
~gunzip data.gz<br>
~ls<br>
~file data<br>
~mv data data.tar<br>
~tar -xf data.tar<br>
~ls<br>
~file data5.bin<br>
~mv data5.bin data5.tar<br>
~tar -xf data5.tar<br>
~ls<br>
~file data6.bin<br>
~mv data6.bin data6.bz2<br>
~bzip2 -d data6.bz2<br>
~ls<br>
~file data6<br>
~mv data6 data6.tar<br>
~tar -xf data6.tar<br>
~ls<br>
~file data8.bin<br>
~mv data8.bin data8.gz<br>
~gunzip data8.gz<br>
~ls<br>
~file data8<br>
~cat data8<br>
***Learnt how to decode a Hexdump using 'xxd', how to unzip bzip2, gzip and tar files and how to use the 'mv' command to rename files***<br>
----------------
**Level 13**<br>
~ls<br>
~ssh -i sshkey.private bandit14@localhost<br>
~yes<br>
~cd /etc/bandit_pass<br>
~ls<br>
~cat bandit1<br>
***Learnt how to use SSH keys to connect***<br>
---------------
**Level 14**<br>
~nc localhost 30000<br>
~4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e<br>
>This is the password for bandit14 which we are asked to forward to port 30000 on localhost<br>
***Learnt how to use Netcat (nc)***<br>
-------------
**Level 15**<br>
~openssl s_client -connect localhost:30001<br>
~BfMYroe26WYalil77FoDi9qh59eK5xNr<br>
>This is the password for bandit15<br>
***Learnt how to use openssl's s_client command to send data with SSL encryption***<br>
