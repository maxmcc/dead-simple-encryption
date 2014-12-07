# CAST is quick cipher, not really broken, small blocks means less padding, changing size
from Crypto.Cipher import CAST
import hmac
import struct
import os

def encrypt_file(input_filename, output_filename):
# hard coded private key from os.urandom for this iteration
	cipher_key = '\xc7\xdfK\xb2\xb1^S\xb9'

	#CBC, or cipher block chaining, hides large scale patterns, bc depends on previous blocks, not just block encrypted
	#since CBC depends on previous chunk, needs IV, or initialization vector, for first chunk
	iv = os.urandom(8)
	obj=CAST.new(cipher_key, CAST.MODE_CBC, IV=iv)

	plain = open(input_filename, 'rb').read()

	rev_mod = 8 - (len(plain) % 8)
	padding_len = 0 if (rev_mod == 8) else rev_mod
	padded_plain = plain + chr(padding_len) * padding_len

	ciph=obj.encrypt(padded_plain)

	# checksum for authentication, hard coded from os.urandom
	authencity_key = '\xbd\xd4q7@W\xa3\xbd'
	h = hmac.new(authencity_key, ciph)

	plain_len = struct.pack('!Q', len(plain))

	f = open(output_filename, 'wb')

	# encrypted file: length + cipher text (+ padding) + MAC (message authentication code)
	h.update(plain_len)
	f.write(plain_len)

	h.update(iv)
	f.write(iv)

	h.update(ciph)
	f.write(ciph)

	f.write(h.digest())
	print "Old MAC: " + h.digest()
	f.close()

def decrypt_file(input_filename, output_filename, authenticity_key, cipher_key):

	encrypted = open(input_filename, 'rb').read()
	print "Encrypted: " + encrypted
	length = len(encrypted)

	# mac is 16 bytes at end

	encrypted_before_MAC = encrypted[:length-16]
	print "Before MAC: " + encrypted_before_MAC
	orig_MAC = encrypted[length-16:]
	print "Old MAC: " + orig_MAC

	computed_MAC = hmac.new(authenticity_key, encrypted_before_MAC).digest()
	print "New MAC: " + computed_MAC

	if hmac.compare_digest(orig_MAC, computed_MAC):
		hex_length = encrypted[:9]
		cipher_length = int(hex_length, 16)#some function from hex to int
		print cipher_length
		iv = encrypted[9: 17]
		cipher_text = encrypted[17:length-20] #-cipher.length]
		obj=CAST.new(cipher_key, CAST.MODE_CBC, IV=iv)
		f = open(output_filename, 'wb')
		temp = obj.decrypt(cipher_text)
		print temp
		f.write(temp)

encrypt_file('secret-file.txt', 'encrypted_file.txt')
decrypt_file('encrypted_file.txt', 'decrypted-file.txt', '\xbd\xd4q7@W\xa3\xbd', '\xc7\xdfK\xb2\xb1^S\xb9')
