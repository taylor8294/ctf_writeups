# Python 3.9
# Reverse engineered from encrypt.py, which was decompiled from encrypt.pyc

with open('announcement_encrypted.md', 'r') as file:
    encrypted_document = [line.replace('\n', '') for line in file.readlines()]

# n (the modulus) = p * q
n = 145906768007583323230186939349070635292401872375357164399581871019873438799005358938369571402670149802121818086292467422828157022922076746906543401224889672472407926969987100581290103199317858753663710862357656510507883714297115637342788911463535102712032765166518411726859837988672111837205085526346618740053
p = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233
q = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
phi = (p-1)*(q-1)
e = 65537 # public exponent

# Need secret exponent d s.t. e * d ≡ 1 mod phi

def extended_euclidean_algorithm(a, b):
    """
    extended_euclidean_algorithm(a, b)

    The result is the largest common divisor for a and b.

    :param a: integer number
    :param b: integer number
    :return:  the largest common divisor for a and b
    """
    if a == 0: return b, 0, 1
    else:
        g, y, x = extended_euclidean_algorithm(b % a, a)
        return g, x - (b // a) * y, y


def modular_inverse(e, z):
    """
    modular_inverse(e, z)

    Calculates modular multiplicative inverse for e and t.

    :param e: in this case e is a public key exponent
    :param z: and z is an Euler function
    :return:  the result of modular multiplicative inverse for e and z
    """
    g, x, y = extended_euclidean_algorithm(e, z)
    if g != 1: raise Exception('Modular inverse does not exist')
    else: return x % z

#d = modular_inverse(e, phi)
#print('d is {}'.format(d))
d = 89489425009274444368228545921773093919669586065884257445497854456487674839629818390934941973262879616797970608917283679875499331574161113854088813275488110588247193077582527278437906504015680623423550067240042466665654232383502922215493623289472138866445818789127946123407807725702626644091036502372545139713

l = len(encrypted_document)
with open('announcement.md', 'w') as confidential_document:
    for i, line in enumerate(encrypted_document):
        print('{}/{} ({}%)'.format(i,l,(100*i)//l), end="\r", flush=True)
        confidential_document.write(chr(pow(int(line), d, n)))

print('{}/{} ({}%) - Decrypted file saved as {}'.format(l,l,100,'announcement.md'))
