#python library with cryptographic hash functions like SHA-256, SHA-1, MD5, etc which will transform data into a fixed-length fingerprint.
#fingerprint is deterministic
#irreversible
#collision-resistant (hard to find matches)
import hashlib

#variable is set to a string value that is unsecured and needs protection.  This info could be exposed, compromised and reused.
secret_message="cybersecurity101"

#cryptography in python begins now

#secret_message.encode() -> covert text string into bytes -> b"cybersecurity101"
#bytes are raw binary data that can be used by cryptographic functions like hashing inside hashlib
#hashlib.sha256(...) takes bytes and runs it thru sha256 algorithm to produce a hash object - a fixed representation of the input data cybersecurity101
#hashed_object is a container holding the computed result and methods to display it
#transformation that happened is irreversible
#output is retrievable but not human-readable

hashed_object=hashlib.sha256(secret_message.encode())


#next step is to extract the fingerprint
#hexdigest() converts binary hash into a readable hexadecimal string
hex_fingerprint=hashed_object.hexdigest()

print("Original Text:", secret_message)
print("SHA-256 Hash :", hex_fingerprint)