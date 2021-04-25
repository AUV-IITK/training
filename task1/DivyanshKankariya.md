# **Commands/Code I used in the questions**


## Logging in and out of each level:
#### ssh login :
ssh username@host -p 0000
#### ssh logout :
used (ctrl +d) or **exit** command.


### lvl 0->1
cat readme


### lvl 1->2
find . -name '-*'
cat ./-


### lvl 2->3
cat 'spaces in this file name'


### lvl 3->4
cd inhere/
ls -a
cat .hidden


### lvl 4->5
cd inhere/
file ./*
*we obsereve that file07 has ASCII text data*
cat ./-file07


### lvl 5->6
cd inhere/
find ./* -size 1033c ! -executable
cat ./maybehere07/.file2


### lvl 6->7
cd /                   *to go to the root directory*
find . -group bandit6 -user bandit7 -size 33c
cat ./var/lib/dpkg/info/bandit7.password


### lvl 7->8
vi data.txt             *opens the file in vi editor*
/millionth              *finds the string millionth*
:q!                     *exits the editor*

**or**
grep -i "millionth" data.txt


### lvl 8->9
sort data.txt|uniq -u     *| sends the sorted output to the uniq command* 


### lvl 9-10
cat data.txt|strings|grep -E "=+"       
                           *-E flag makes it valid to use the = operater here*



## **Divyansh Manakchand Kankariya software assignment**


 








