
Given the following string
```
617a316a5a6d526a4d44466c4f54526d5a4463794f4445354d5455354f444d77593255344e54646d597a45354d437870505446684f57526c5a6a6b344e57457a4d7a49334e6a59784d6d49314d6a4532596a5a6a5a6a4e6b4d5755344c4449774f5446685a444d325a444d324d574d344f475131597a4d794d444a6c4d7a5a6b4f546331595441314e4455314e5464694e4455775a44566d5a47466d5954466b4e6a49774e7a6c6d4d5749324e6a677a59544a6b4e574e6c595459335a5759774f47557a4d6d4533595445314f4755315932526b4d7a67304f44557a5a413d3d
```

From Hex, From Base-64
```
k=cfdc01e94fd72819159830ce857fc190
i=1a9def985a33276612b5216b6cf3d1e8
2091ad36d361c88d5c3202e36d975a0545557b450d5fdafa1d62079f1b6683a2d5cea67ef08e32a7a158e5cdd384853d
```

Looks like 16 byte key, 16 byte IV, and resulting ciphertext... but what encryption is used..? 

"twisting seA" == "AES" ?

But trying to simply decrypt as AES gives

```
l¬.¿k.el.ìWm8ôÕ.c1EEe20DE59F8dfcA2bd06e}
```

Playing revealed IV is UTF8 encoded, not raw hex! See [CyberChef Recipe](https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'Hex','string':'cfdc01e94fd72819159830ce857fc190'%7D,%7B'option':'UTF8','string':'1a9def985a33276612b5216b6cf3d1e8'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=MjA5MWFkMzZkMzYxYzg4ZDVjMzIwMmUzNmQ5NzVhMDU0NTU1N2I0NTBkNWZkYWZhMWQ2MjA3OWYxYjY2ODNhMmQ1Y2VhNjdlZjA4ZTMyYTdhMTU4ZTVjZGQzODQ4NTNk)

```
AES_Decrypt({'option':'Hex','string':'cfdc01e94fd72819159830ce857fc190'},{'option':'UTF8','string':'1a9def985a33276612b5216b6cf3d1e8'},'CBC','Hex','Raw',{'option':'Hex','string':''},{'option':'Hex','string':''})
```

Giving our flag: `GPSCTF{208E5f02Dc1EEe20DE59F8dfcA2bd06e}`.