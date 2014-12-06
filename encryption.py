# CAST is quick cypher, not really broken, small blocks means less padding, changing size
from Crypto.Cipher import DES

from hmac import *

#CBC or cypher block chaining hides large scale patterns, bc depends on previous blocks, not just block encrypted

# def encrypt_file(filename):
# hard coded private key from os.urandom for this iteration
cypher_key = '\xc7\xdfK\xb2\xb1^S\xb9'
obj=DES.new(cypher_key, DES.MODE_ECB)
plain="Guido van Rossum is a space alien."

padded_plain = plain

# PKCS7 padding better than zero padding
mod = len(padded_plain) % 8
if (mod != 0):
	for i in range(8-mod):
		padded_plain = padded_plain + str(i)

ciph=obj.encrypt(padded_plain)

# checksum for authentication
checksum_padded_plain = padded_plain

authencity_key = '\x17\xd1\x08k\x9d\xfa\xd3\xb3'
# h = hmac.new(authencity_key, ciph)

print ciph

f = open('encrypted_file.txt', 'w')

f.write(ciph)

# def decrypt_file(file):
# obj=DES.new('abcdefgh', DES.MODE_ECB)
# plain = read from 
# retrieve hmac from cypher text

# take cypher text, compute digest, compare to actual digest

#if equal, obj.decrypt(ciph)