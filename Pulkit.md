1.  Level 0    ssh

2.  Level 1    cd ~   (current directory)
               ls -alh  (display all the files contained in the direactory)
               cat   (to read the file)
               password boJ9jbbUNNfktd78OOpsqOltutMc3MY1
               ssh    to log into bandit1

3.  Level 2    cat ./-    (to put dash in front of the file name)
               pass    CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

4.  Level 3    cat  \  (backslash space)(to put space in file name)
               pass    UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

5.  Level 4    cd command to enter the directory
               cat the file
               pass    pIwrPrtPN36QITSp3EQaw936yaFoFgAB

6.  Level 5    pass    koReBOKuIDDepwhWk7jZC0RTdopnAYKh

7.  Level 6    find . -size 1033c ! -executable  (to search the file by size and based on execution)
               pass    DXjZPULLxYr17uwoI01bNLQbtFemEgo7

8.  Level 7    first go into the root directory using "cd /"
               and then find the file using "find / -user bandit7 -group bandit6 | grep bandit7"
               and then cat the file as "cat `find . -size 33c -group bandit6 -user bandit7 2>/dev/null`"
               pass    HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

9.  Level 8    simply used grep as "grep  "millionth" data.txt".It will search the word under the given file and display the given line.
               pass    cvX2JJa4CFALtqS87jk27qwqGhBM9plV

10. Level 9    "sort data.txt | uniq -c | grep 1\ ?*"
               sort statement sort the strings in the file data.txt and uniq filter out the duplicate ones and grep 1\ ?* used to display the line which occured only once.
               pass    UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

11. Level 10   used first strings to print the printable characters and then filtered out using grep.
               "strings data.txt | grep "====="
               pass    truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk





