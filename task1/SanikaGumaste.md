Level 0: $ ssh bandit0@bandit.labs.overthewire.org -p 2220
         Entered password successfully. 
Level 1:  ls
          readme
          cat readme
          Obtained password
          Exit level 1
Level 2: $ ssh bandit1@bandit.labs.overthewire.org -p 2220
          Entered password successfully
           ls -a
           cat ./-
           Obtained password
           Exit level 2
Level 3: $ ssh bandit2@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          dir
          spaces\ in\ this\ filename
          cat spaces\ in\ this\ filename
          Obtained password
          Exit level 3
Level 4: $ ssh bandit3@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          ls
          inhere
          cd inhere
          ls -a
          cat .hidden
          Obtained password
          Exit level 4
 Level 5: $ ssh bandit4@bandit.labs.overthewire.org -p 2220
          Entered password successfully 
          ls -a
          cd inhere
          ls -a
          file ./-*
          cat ./-file07
          Obtained password
          Exit level 5
Level 6: $ ssh bandit5@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          ls
          inhere
          cd inhere
          ls -a
          find -type f -size 1033c
          cat ./maybehere07/.file2
          Obtained password
          Exit level 6
Level 7: $ ssh bandit6@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          find / -user bandit7 -group bandit6 -size 32c 2>/dev/null ar/lib/dpkg/info/bandit7.password
          /var/lib/dpkg/info/bandit7.passwordcat /var/lib/dpkg/info/bandit7.password 
          cat /var/lib/dpkg/info/bandit7.password
          Obtained password
          Exit level 7
Level 8: $ ssh bandit7@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          ls -a
          awk '/^millionth/ {print $2;}' data.txt
          Obtained password
          Exit level 8
Level 9: $ ssh bandit8@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          ls -a
          cat data.txt | sort | uniq -u
          Obtained password
          Exit level 9
Level 10: $ ssh bandit9@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          ls -a
          strings data.txt | grep "="
          Obtained password
          Exit level 10
Level 11:  $ ssh bandit10@bandit.labs.overthewire.org -p 2220
          Entered password successfully
          ls -a
          cat data.txt
          VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg==
          echo VGhlIHBhc3N3b3JkIGlzIElGdWt3S0dzRlc4TU9xM0lSRnFyeEUxaHhUTkViVVBSCg== | base64 --decode
          Obtained password
          Exit level 11.

