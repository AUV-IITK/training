## Level 0

### Codes

> ssh bandit0@bandit.labs.overthewire.org -p 2220

### Learning

I learnt the use of ssh command. I had to read up about how to install and run it on ubuntu. I ran into the problem of wrong port.
I had to use the _man_ command to get the correct command.

---

## Level 1

### Codes

> ls
>
> cat readme

---

## Level 2

### Codes

> cat ./-

### Learning

Learnt the use of relative path. Earlier I was using only /- (similar to C++ for special characters). I had to look up the use of relative path, the use of ./

---

## Level 3

### Codes

> cat "spaces in this filename"

---

## Level 4

### Codes

> ls -al
>
> cd inhere/
>
> cat ".hidden"

---

## Level 5

### Codes

> ls
>
> cd inhere/
>
> strings ./-file*

### Learning

I learnt the use of strings command to display printable characters in the file. I also learnt the use of \* (meaning "zero or more characters") after file name to iterate over all files starting with a particular name like a0,a1, etc.

---

## Level 6

### Codes

> ls
>
> cd inhere/
>
> find . -type f -readable ! -executable -size 1033c
>
> cat maybehere07/-file2

### Learning

I learnt the use of find command an the various tests related to find using man find command.

---

## Level 7

### Codes

> find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
>
> cat /var/lib/dpkg/info/bandit7.password

### Learning

I learnt that for current directory symbol used is (.) and for root directory (/) is used. Also i learnt that > operator redirects output to a file.

1> file redirects stdout to file (or > file)
2> file redirects stderr to file
&> file redirects stdout and stderr to file (or > file 2>&1)

/dev/null is the null device it takes any input you want and throws it away. It can be used to suppress any output.

---

## Level 8

### Codes

> cat data.txt | grep millionth

### Learning

I learnt the following:

- Pipe (|): The Pipe is a command in Linux that lets us use two or more commands such that output of one command serves as input to the next. Similar to and in boolean algebra.
- Grep (grep): Used to match texts in a file. It is used to search a particular string in a file.
  - -v: Shows all the lines that do not match the searched string
  - -c: Displays the number(count) of matching lines
  - -n: Shows the matching line and its number(line number in file)
  - -i: Match both (upper and lower) case
  - -l: Shows just the name of the file with the string
- Sort (sort): Used to sort the contents of the file
  - -r: Reverses sorting
  - -n: Sorts numerically
  - -f: Case insensitive sorting

---

## Level 9

### Codes

> cat data.txt | sort | uniq -u

### Learning

Uniq command:

- -c: giveb the number of times each line occurs
- -d: only prints the duplicate lines (only once)
- -D: print all duplicate lines (all occurances)
- -f=N: avoid comparing the first N fields
- -i: ignore differences in case when comparing
- -u: only print unique lines

I was earlier not using sort. Then on reading documantation of uniq I learnt that it isn’t able to detect the duplicate lines unless they are adjacent. So I had to use sort to help in the process.

---

## Level 10

### Codes

> strings data.txt | grep =

---

## Level 11

### Codes

> cat data.txt | base64 --decode

### Learning

I learnt the base64 command and how to decode and encode using the command.

---

## Level 12

### Codes

> cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'

### Learning

I was earlier trying using multiple tr commands but it was not working. I then had to look up the correct way to write the command to get the result

---

## Level 13

### Codes

> mkdir /tmp/ritam123
>
> cp data.txt -t /tmp/ritam123
>
> cd /tmp/ritam123
>
> file data.txt
>
> xxd -r data.txt > file0
>
> file file0 (file was compressed in gzip format)
>
> mv file0 file1.gz
>
> gzip -d file1.gz
>
> file file1 (file was compressed in bzip2 format)
>
> mv file1 file3.bz2
>
> bzip2 -d file3.bz2
>
> file file3 (file was compressed in gzip format)
>
> mv file3 file4.gz
>
> gzip -d file4.gz
>
> file file4 (file was compressed from tar format)
>
> tar -xvf file4
>
> file data5.bin (file was compressed from tar format)
>
> tar -xvf data5.bin
>
> file data6.bin (file was compressed in bzip2 format)
>
> mv data6.bin file5.bz2
>
> bzip2 -d file5.bz2
>
> file file5 (file was compressed from tar format)
>
> tar -xvf file5
>
> file data8.bin (file was compressed in gzip format)
>
> mv data8.bin file6.gz
>
> gzip -d file6.gz
>
> file file6 (ASCII Text file)
>
> cat file6

### Learning

Learnt the ways of compressing and decompressing files using gzip, bzip2 and tar formats.
I earlier used tar -x and tar -xvzf to extract but got error. On researching, realised that i have to use tar -xvf.

---

## Level 14

### Codes

> ssh bandit14@localhost -i sshkey.private
>
> cd etc/
>
> cd bandit_pass/
>
> cat bandit14

### Learning

The use of -i to use the private ssh key stored in one's computer.
Find the location od password file in /etc folder.

---

## Level 15

### Codes

> telnet localhost 30000

### Learning

I learned the use of telnet to connect to different ports in the same ssh server.
