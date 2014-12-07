dead-simple-encryption
======================

Created at Google's Hack4Humanity 2014 by Yoni Nachmany, Annie Meng, Max McCarthy, Ben Sandler, and William Archer.


# Problem:
Private files are no longer private files. This problem extends from the sphere of journalism to dissidents, and impacts anyone who faces risk of government crackdown and the possibility of incriminating data. In places without secure internet connection, it's often hard to upload this data to the cloud and most other encryption software has a high barrier to entry for non-technical users. The files however must be securely encrypted and hidden. 

# What we do
We took all these things and created an easy to use executable that encrypts given files and hides their segments within other safe files on your computer, employing the secure method of steganography. It also associates a password of your choice with the encryption and is needed to decrypt the files - making sure only you can decrypt. Upon encryption, a zip directory is produced containing components of your sensitive files injected into safe files, removing all evidence of their real content.

# Features:
## Easy to use interface
Simple launch the app and drag and drop your desired files. Enter a password. Either encrypt or decrypt. No learning curve, no stress.

## Secure storage 
The contents of your sensitive files get encrypted with standard AES procedures and combined with steganography to split your files into unsuspicious compressed files. No one who opens it knows what you're hiding. Security by obfuscation and security by confusion.

## No remaining evidence
Our app doesn't need to be left on your system to decrypt the files again. Easily delete the app to hide any evidence you used it and simply re-download it to get back your files.

# Tech Used
Python backend for encryption and steganography. JS, Sass and HTML front end. Node app wrapped with node-webkit for cross-platform compatibility. 

