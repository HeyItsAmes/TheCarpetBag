#hashlib python library with cryptographic hash functions like SHA-256, SHA-1, MD5, etc which will transform data into a fixed-length hash
#Deterministic output: same input, same hash. Different input, diff hash.
#irreversible, one-way - used to verify, not recover
#Reproducable
import hashlib

#variable is set to a string value that is unsecured and needs protection. Could be exposed, compromised and reused.
secret_message="cybersecurity101"

#cryptography in python begins now

#secret_message.encode() -> covert text string into bytes -> b"cybersecurity101"
#bytes are raw binary data that can be used by cryptographic functions like hashing inside hashlib
#hashlib.sha256(...) takes bytes and runs it thru sha256 algorithm to produce a hash object - a fixed representation of the input data cybersecurity101
#hashed_object is a container holding the computed result and methods to display it
#transformation that happened is irreversible
#output is retrievable right now but not human-readable

hashed_object=hashlib.sha256(secret_message.encode())


#extract the hash, use hexdigest() to convert binary hash into a readable hexadecimal. Hexadecimal is the standard format used across systems.
hex_output=hashed_object.hexdigest()

print("Original Text:", secret_message)
print("SHA-256 Hash :", hex_output)


# Example Output:
# (When secret_message = "cybersecurity101")
#
# Original Text: cybersecurity101
# SHA-256 Hash : 189353bca1b7a01c5116fabd80ffc5d751cd6c7cc417a21ff75cfb51ab060db3