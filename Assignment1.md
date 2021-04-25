# Assignment-1

<hr style="border:1px solid gray"> </hr>

## OverTheWire Wargames (Bandit) Lvl 0-10

<hr style="border:1px solid gray"> </hr>


#### Login


##### Code
>ssh bandit0@bandit.labs.overthewire.org  -p 2220
---

#### Level 0-

##### Code
>ls
>
>cat readme

---

#### Level 1-
##### Code
> cat ./-


---

#### Level 2-
##### Code
>cat spaces\ in\ this\ filename

---

#### Level 3-
##### Code
>cd inhere/
>
>ls -a
>
>cat .hidden

---

#### Level 4-
##### Code
>cd inhere
>
>file ./-*
>
>cat ./-file07

*file07-only file with ASCII text*

---

#### Level 5-
##### Code
>cd inhere
>
>find ./maybehere* -size 1033c
>
>cat ./maybehere07/.file2

*-size used to find file with given size (c for bytes)*

---
#### Level 6-
##### Code
>find  / -user bandit7 -group bandit6 -size 33c
>
>cat  /var/lib/dpkg/info/bandit7.password


---

#### Level 7-
##### Code
>grep 'millionth' data.txt

---

#### Level 8-
##### Code
>sort data.txt | uniq -u

*sort is used first to put same text adjacent to each other which is then filtered by uniq and printed using -u*

---

#### Level 9-
##### Code
>strings data.txt | grep '===='

---

#### Level 10-
##### Code
>base64 -d data.txt
