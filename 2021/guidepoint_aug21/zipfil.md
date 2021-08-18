The zip file we are given does not open.

Looking at the files hex, it is missing the correct magic bytes for a PZIP file, namely `50 4b 03 04`.

```
00 00 00 00 00 e8 00 00 00 e4 00 10 00 10 00 00
00 00 60 50 b4 05 00 00 00 00 40 00 00 00 00 40
10 00 b0 87 57 d5 c8 9d 91 30 00 50 45 55 47 87
47 e2 76 16 c6 66 00 00 00 00 18 4a 00 00 00 10
00 00 00 00 00 81 00 80 00 00 00 03 00 00 00 c3
86 86 e8 c9 f4 a3 b5 d8 00 00 00 90 00 a0 30 e1
20 10 b4 05 00 00 00 03 00 00 00 c3 86 86 e8 c9
80 70 b4 05 d4 29 68 c0 6f d0 5f 87 9e d2 1e 54
60 e5 79 4f 80 d2 8c 4d e8 0a f2 17 cb 9b 28 a5
1c f3 b6 55 11 63 c3 1c ca 92 8e cd 0e 7e f6 cd
9e ef 55 b8 9d f4 38 2b 85 25 59 ea f1 d7 87 bd
00 00 00 00 40 00 00 00 00 40 10 00 b0 87 57 d5
c8 9d 91 d5 c8 9d 91 30 00 90 45 55 47 87 47 e2
76 16 c6 66 00 c1 00 80 00 00 00 03 00 00 00 c3
86 86 e8 c9 f4 a3 b5 d8 00 00 00 90 00 a0 40 30
b4 05
```

I tried replacing the first 4 null bytes, also tried prepending them to the file, but neither resulted in a valid ZIP file. Looking closely, you may notice the last 4 bytes... `40 30 b4 05`... its reversed!

Reversing the hex gives us

```
50 4b 03 04 0a 00 09 00 00 00 8d 5b 3a 4f 9c 8e
68 68 3c 00 00 00 30 00 00 00 08 00 1c 00 66 6c
61 67 2e 74 78 74 55 54 09 00 03 19 d9 8c 5d 19
d9 8c 5d 75 78 0b 00 01 04 00 00 00 00 04 00 00
00 00 db 78 7d 1f ae 95 52 58 b2 83 4f d9 8b 55
fe e9 dc 6f e7 e0 dc e8 29 ac c1 3c 36 11 55 6b
3f c1 5a 82 b9 bc 71 2f a0 8e d4 c8 2d 08 f4 97
5e 06 45 e1 2d e9 78 f5 0d f6 0c 86 92 4d 50 4b
07 08 9c 8e 68 68 3c 00 00 00 30 00 00 00 50 4b
01 02 1e 03 0a 00 09 00 00 00 8d 5b 3a 4f 9c 8e
68 68 3c 00 00 00 30 00 00 00 08 00 18 00 00 00
00 00 01 00 00 00 a4 81 00 00 00 00 66 6c 61 67
2e 74 78 74 55 54 05 00 03 19 d9 8c 5d 75 78 0b
00 01 04 00 00 00 00 04 00 00 00 00 50 4b 05 06
00 00 00 00 01 00 01 00 4e 00 00 00 8e 00 00 00
00 00
```

which is a valid ZIP and contains our `flag.txt` file!.. But it needs a password.

Using zip2john (or an equivalent [online tool](https://www.onlinehashcrack.com/tools-zip-rar-7z-archive-hash-extractor.php)) we can extract the hash, which is

```
$pkzip2$1*2*2*0*3c*30*68688e9c*0*42*0*3c*6868*5b8d*db787d1fae955258b2834fd98b55fee9dc6fe7e0dce829acc13c3611556b3fc15a82b9bc712fa08ed4c82d08f4975e0645e12de978f50df60c86924d*$/pkzip2$
```

I used [Hashcat](https://github.com/someshkar/colabcat) to try brute force the flag using the 

```bash
hashcat -m 17210 /root/.hashcat/hashes/zipfil.txt /root/wordlists/SecLists/Passwords/Leaked-Databases/rockyou-75.txt
```

And it got it almost instantly as `123456`. Extracting the file using the password, gives us the flag inside flag.txt: `StormCTF{Misc2:B73dba52ceDA4dDccb31Ec1b1cDa24Ff}`.