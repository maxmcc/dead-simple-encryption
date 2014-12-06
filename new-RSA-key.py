from Crypto.PublicKey import RSA
key = RSA.generate(2048)
f = open('mykey.pem','w')
f.write(RSA.exportKey('PEM'))
f.close()

f = open('mykey.pem','r')
key = RSA.importKey(f.read())