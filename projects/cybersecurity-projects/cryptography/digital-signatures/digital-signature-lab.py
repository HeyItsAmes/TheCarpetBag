# Cryptography Lab 1: SHA-256 Hashing
# Concept: Data Integrity 
# Security+: Hash Functions, Integrity, One-way functions
# Self-directed cybersecurity lab Security+ SY0-701 aligned Cryptography fundamentals

import hashlib

message="Version 2.1 Security Patch"

#use the hash libary module to convert message str into bytes then sha256 algorithm function to turn bytes a python object containing hash info and methods (one-way cryptogrpaphic obj)
hash_object=hashlib.sha256(message.encode())

#convert into human readable hexadecimal
hash_hex=hash_object.hexdigest()

print(message) #original message
print(hash_hex) #hexadecimal representation of the hash

#this program gives integrity that the message wasn't changed but doesn't answer if the patch sender is verified as the original sender (digital signature for authentication and non-repudiation)
#private key used to sign (real world sender would encrypt hash w private key)
#public key used to verify








