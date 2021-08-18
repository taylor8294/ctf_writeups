File is corrupt, only shows up to packet #901

HackTricks has a useful page on [Pcap Inspection](https://book.hacktricks.xyz/forensics/basic-forensic-methodology/pcap-inspection) the points us to [http://f00l.de/hacking/pcapfix.php](http://f00l.de/hacking/pcapfix.php) for fixing corrupted captures. Trying it out, it finds 2 issues and does fix our file! The fixed file now shows 926 packets.

Packet #902 looks interesting...

```
0000   40 ce 93 a2 01 88 ff ff 43 03 81 06 01 00 2d 00   @.......C.....-.
0010   a2 6b b3 53 00 00 00 00 c5 e7 06 00 00 00 00 00   .k.S............
0020   00 02 00 00 00 02 00 00 00 00 00 00 00 00 00 00   ................
0030   00 00 00 00 00 00 00 00 01 02 00 00 00 00 00 00   ................
0040   55 33 52 76 63 6d 31 44 56 45 5a 37 54 57 6c 7a   U3Rvcm1DVEZ7TWlz
0050   59 7a 49 36 4e 7a 5a 6c 52 6a 45 79 4e 44 45 32   YzI6NzZlRjEyNDE2
0060   4d 7a 63 32 4d 30 49 7a 4e 54 4a 43 4f 54 67 34   Mzc2M0IzNTJCOTg4
0070   59 30 4a 42 4d 57 55 33 4e 7a 56 42 4f 45 46 39   Y0JBMWU3NzVBOEF9
```

A quick recipe in [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hexdump()From_Base64('A-Za-z0-9%2B/%3D',true)&input=MDA0MCAgIDU1IDMzIDUyIDc2IDYzIDZkIDMxIDQ0IDU2IDQ1IDVhIDM3IDU0IDU3IDZjIDdhICAgVTNSdmNtMURWRVo3VFdsegowMDUwICAgNTkgN2EgNDkgMzYgNGUgN2EgNWEgNmMgNTIgNmEgNDUgNzkgNGUgNDQgNDUgMzIgICBZekk2TnpabFJqRXlOREUyCjAwNjAgICA0ZCA3YSA2MyAzMiA0ZCAzMCA0OSA3YSA0ZSA1NCA0YSA0MyA0ZiA1NCA2NyAzNCAgIE16YzJNMEl6TlRKQ09UZzQKMDA3MCAgIDU5IDMwIDRhIDQyIDRkIDU3IDU1IDMzIDRlIDdhIDU2IDQyIDRmIDQ1IDQ2IDM5ICAgWTBKQk1XVTNOelZCT0VGOQ) and we have our flag!