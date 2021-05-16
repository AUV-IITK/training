*Level 0*
ssh bandit0@bandit.labs.overthewire.org -p 2220

*Level 1*
used cat readme to veiw readme file

Password : boJ9jbbUNNfktd78OOpsqOltutMc3MY1

*Level 2*
used cat< - to view dashed file

Password : CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

*Level 3*
used cat spaces\ in\ this\ filename
we can also use cat "spaces in this filename"

Password :UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

*Level 4*
cd inhere/
ls (file was hidden)
ls -a
cat .hidden

Password : pIwrPrtPN36QITSp3EQaw936yaFoFgAB

*Level 5*
used  file inhere/* to get the type of each file.*
inhere/-file00: data
inhere/-file01: data
inhere/-file02: data
inhere/-file03: data
inhere/-file04: data
inhere/-file05: data
inhere/-file06: data
inhere/-file07: ASCII text
inhere/-file08: data
inhere/-file09: data
then used cat< -file07 to read password.

Password: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

*Level 6*
find . -size 1033c ! -executable
to get the file location (./maybehere07/.file2)
cat ./maybehere07/.file2
Password: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

*Level 7*
find / -user bandit7 -group bandit6 -size 33c for most of the file it showed permission denied, and then i looked for the read only file.
/var/lib/dpkg/info/bandit7.password
then i extract the password using cat /var/lib/dpkg/info/bandit7.password
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

*Level 8*
used grep "millionth" data.txt
output was : millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV

*level 9*
cat data.txt | sort | uniq -c -u
      1 UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
the sort command sort the txt file so that same strings are adjacent to each other and with the help of uniq command it gives the desired output
-c count the number of repeated line
-u prints the unique line

*Level 10*
used strings data.txt | grep -F "=" 
the string command prints the human readable text and grep -F search for the patter as fixed strings.

Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

*Level 11*
used base64 data.txt -d
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
base64 command use to encode and decode the data from base64 file.
-d use to decode the text in ASCII
-e encode it.

