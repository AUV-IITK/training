## TASK 1 
### overthewire-BANDIT
###### by Om Jee

#### level 0.
 cat readme // cat command prints the contents of the file
#### level 1.
 cat ./-   
#### level 2.
 cat "spaces in this filename" // enclosing within "" ignores the spaces in file name   
#### level 3.
 cd inhere  // moved to inhere directory
 ls -al   // lists all the files
 cat .hidden   
#### level 4.
 cd inhere   
 file ./*  //-file07 was in ASCII code
 cat ./-file07   
#### level 5.
 cd inhere  
 find ./ -type f -readable ! -executable -size 1033c   
 cat ./maybehere07/.file2   
#### level 6.
 find / -user bandit7 -group bandit6 -size 33c  
 cat /var/lib/dpkg/info/bandit7.password  
#### level 7.
 ls  
 cat ./data.txt | grep "millionth" // grep prints the entire line containing the word millionth 
#### level 8.
 ls
 cat ./ data.txt | sort | uniq -u  // sort command sroted the file and then uniq -un printed the only unique line
#### level 9.
 ls
 strings ./data.txt | grep -E "==+" 
#### level 10.
 ls  
 cat ./data.txt | base64 -d   

