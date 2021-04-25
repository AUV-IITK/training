### Level 0
About SSH
```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
Then it asks the password bandit0 and we get access.

---

### Level 0 -> Level 1
Password: 'boJ9jbbUNNfktd78OOpsqOltutMc3MY1' by viewing readme file.

Same ssh method as in level 0, this time to the user bandit1.

---
### Level 1 -> Level 2
Weird thing to open - files ```cat < -```.

Password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9 (vim copying thing doesn't work somehow)

ssh to next level.

---
### Level 2 -> Level 3
Easy  ```cat *```.

Password:UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

---
### Level 3 -> Level 4
```bash
cd inhere
ls -la
cat .hidden
```
Password:pIwrPrtPN36QITSp3EQaw936yaFoFgAB

---
### Level 4 -> Level 5
Went to that folder and cat every file (07 one had the password).

Password:koReBOKuIDDepwhWk7jZC0RTdopnAYKh

---
### Level 5 -> Level 6

```bash
cd ./inhere
ls -la ./*
```
Then copied all the results into a text file and opened it in sublime, used ctrl+f to find that 1033 bytes file (only in maybehere07 directory)

```-rw-r-----  1 root bandit5 1033 May  7  2020 .file2```

Password:DXjZPULLxYr17uwoI01bNLQbtFemEgo7

---
### Level 6 -> Level 7
Used find command here.

Checked two possible locations/files
 - ./var/lib/dpkg/info/bandit7.password -> cat worked here
 - ./etc/bandit_pass/bandit7 -> Permission denied

```bash
find ./* -user bandit7
```
Password: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

---
### Level 7 -> Level 8
used grep as the file was really large and copying that to open is sublime would take too long.

```bash
grep -R data.txt -e 'millionth'
```
-R stands for recursive here

-e for the pattern to find

Password: cvX2JJa4CFALtqS87jk27qwqGhBM9plV

---
### Level 8 -> Level 9

Copied everything from data.txt (1001) and then ran a program.
```python
f = open("data.txt", "r")
cnt = {}
while True:
    line = str(f.readline())
    if not line:
        break

    if line in cnt:
        cnt[line] += 1;
    else:
        cnt[line] = 1;


for c in cnt:
    if cnt[c] == 1:
        print(c)
        break

f.close()
```

Password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR

---
### Level 9 -> Level 10
cat data.txt
Saw those ====== and used the string next to it.

Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk

---
### Level 10 -> Level 11
```bash
base64 -d data.txt
```
Password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

---
### Level 11 -> Level 12
Used [this to decode](https://www.boxentriq.com/code-breaking/rot13)

Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu

---
### Level 12 -> Level 13
Was stuck on this level for quite some time. What I did:
- copied data from data.txt and pasted it in my local machine as random.txt
- used ```cat random.txt | xxd -r > unzipper.gz ``` to create the zip from hexdump
- pressed ```extract here``` button a lot of times from there.

```bash
unzipper (1)
├── data5
│   ├── data6
│   │   ├── data8
│   │   └── data8.bin
│   └── data6.bin
└── data5.bin
```
This was the structure, finally and password was in data8.

Password:8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

---
### Level 13 -> Level 14
```bash
ssh bandit14@localhost -i sshkey.private
```
This was different from other levels. Used ssh inside the bandit13 user to get into bandit14 then can get the password from the specified folder.

Password: 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

---
### Level 14 -> Level 15

Nice lesson on how to interact with other ports.

```
telnet localhost 30000
```
This was to make connection to localhost.
Then entered my current known password to get the next password as response.

(found about something called netcat but the documentation was confusing so used telnet instead to make connection).

Password: BfMYroe26WYalil77FoDi9qh59eK5xNr


---
### Level 15 -> Level 16

Here telnet won't work as it won't use ssl encryption.
```bash
openssl s_client -connect localhost:30001
```
Used [openssl](https://superuser.com/questions/346958/can-the-telnet-or-netcat-clients-communicate-over-ssl) instead.

Password: cluFn7wTiGryunymYOu4RcffSxQluehd


---
### Level 16 -> Level 17

