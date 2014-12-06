from Crypto.Hash import MD5
from Crypto.PublicKey import RSA
from Crypto import Random
rng = Random.new().read
RSAkey = RSA.generate(2048, rng)   # This will take a while...
f = open('secret-file.txt', 'r')
plaintext = f.read()
hash = MD5.new(plaintext).digest()
signature = RSAkey.sign(hash, rng)
signature   # Print what an RSA sig looks like--you don't really care.
RSAkey.verify(hash, signature)     # This sig will check out