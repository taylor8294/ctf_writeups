```python
import math

# use provided script to base64 decode the key file
encrypted_data = [7694194,16350475,36749787,26848661,24851007,25419633,16955316,8403412,24623603,8714007,3092738,20170050,2768005,21734600,1831523]
common_key = [(1, 50041451), (24494333, 42316523), (34771207, 38278327), (52840583, 54931427), (20563681, 37135897), (18560735, 33916541), (14186273, 21349087), (16829987, 29217563), (4792727, 46912927), (7884109, 13664641), (4118885, 17867071), (5379809, 20227751), (981769, 16148053), (25971193, 32882891), (16111231, 19301609)]
private_key = [(1, 1), (31907969, 29944299), (30087427, 28267924), (19054339, 49766097), (33806909, 14876694), (13211339, 25021943), (19859297, 10292487), (28789067, 27988524), (34994987, 42920099), (7155643, 12840606), (9516259, 13595233), (9276227, 16968522), (4098053, 6646150), (31877551, 22722611), (16594581, 7036173)]

# Method in script provided:
#     x = (a ** b) ** (c ** d)
#     c1 = chr((x % n) % 256)
#     c2 = chr((x % n) // 256 % 256)
#     c3 = chr((x % n) // 65536)
# Will never execute as exponents are too large!
# We can use the fact x is only used modulo n to avoid these.

# Recall modulo distributes multiplicitively, that is:
# A*B mod N = (A mod N) * (B mod N) mod N
# => A^B mod N = ((A mod N) * (A^(B-1) mod N)) mod N
# => A^B mod N = ((A^(B/2) mod N) * (A^(B/2) mod N)) mod N etc
# => A^B mod N = (A mod N)^B mod N

# Use this to quickly calculate any power, modulo some number,
# by breaking up the number up into powers of two, and relying
# on squaring previous results to get to the answer
# (see https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation)

# just used to quickly get what powers of two we need
def getbits(n,b=0):
    if b:
        return list(reversed(list(map(int,'{num:0{width}b}'.format(num=n, width=b)))))
    return list(reversed(list(map(int,"{0:b}".format(n)))))

# Efficiently calculates a^b mod n where b is very large 
def powmod(a,b,n):
    bits = list(enumerate(getbits(b)))
    results = {}
    for i, bit in bits:
        if(i == 0):
            results[0] = a % n
        else:
            results[i] = pow(results[i-1], 2, n)
    prod = 1
    for i in [i for (i,bit) in bits if bit]:
        prod = (prod * results[i]) % n
    return prod

# So we have
# (a**b)**(c**d) % n = powmod(a**b, c**d, n)
#                    = powmod(powmod(a, b, n), c**d, n) by distributive property
#                                        but this^ is a problem... Euler's theorem to the rescue!

# Euler's totient function:
# the number of positive integers less that or equal to n that are relatively prime to n.
def phi(n):
    result = n                  # start by assuming all are coprime 
    i = 2                       # use a sieve method starting from 2 
    while i*i <= n:             # working up to sqrt(n)
        if n % i == 0:          # if not coprime
            while n % i == 0:   # can reduce the search down to smallest factor
                n //= i
            result -= result//i # getting rid of all multiples of i
        else:
            i += 1              # if is coprime, can move on
    if n > 1:
        result -= result//n     # lastly, remove remaining multiples of smallest factor we ended on
    return result

# Euler's theorem states a**phi(n) == 1 mod n, where a and n are coprime
# So given powmod(a, b, n) and n are coprime... we know
# powmod(powmod(a, b, n), c**d, n) = powmod(powmod(a, b, n), c**d % phi(n), n)
#                                  = powmod(powmod(a, b, n), powmod(c, d, phi(n)), n)

for a, (b,n), (c,d) in zip(encrypted_data, common_key, private_key):
    y = powmod(powmod(a, b, n), powmod(c, d, phi(n)), n)
    c1 = chr(y % 256)
    c2 = chr(y // 256 % 256)
    c3 = chr(y // 65536)
    print(c3, c2, c1, sep='', end='', flush=True)
print('', flush=True) # Flag is "ugra_it_is_too_powerful_rsa_right_ffccc1abff6"

print("Decoding finished!")
# Runs in 0.016 seconds on my CPU (1.6GHz, 4 core, 8LP)
```
