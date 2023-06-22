#No pip required, part of standard library
import ucryptolib

#Something like ucryptolib can be good when sending data over a tranciever or some form of wireless communication

#16bit - Come up with a 16 character sting to input into ucryptolob.aes command below.
#In this example I'm using feijIJ39%$%DfJVi, note you could also put this value in a secrets.py
enc = ucryptolib.aes(b'feijIJ39%$%DfJVi', 1)
#Input the string you wish to encrypt
data = 'test this data that I would like to encode and then decode'
#Create your data_bytes variable
data_bytes = data.encode()
#Encrypt your string.  This will outbput your encrypted data.  You can then transmit this
test = enc.encrypt(data_bytes + b'\x00' * ((16 - (len(data_bytes) % 16)) % 16))

#Lets pretend the following is on the device that has recieved your transmitted data
#Use the same 16 character string to decrypt the message as you used to encrypt...
dec = ucryptolib.aes(b'feijIJ39%$%DfJVi', 1)
#Decrypt the string, decode the byte string, and get rid of any extra \x00's on the end 
dec.decrypt(test).decode().replace('\x00','')


#32bit?
enc = ucryptolib.aes(b'feijIJ39%$%DfJVifeijIJ39%$%DfJVi', 1)
data = 'test this data that I would like to encode and then decode'
data_bytes = data.encode()
test = enc.encrypt(data_bytes + b'\x00' * ((32 - (len(data_bytes) % 32)) % 32))
dec = ucryptolib.aes(b'feijIJ39%$%DfJVifeijIJ39%$%DfJVi', 1)
dec.decrypt(test).decode().replace('\x00','')
