# Cryptography Lab 1: SHA-256 Hashing and Digital Signature
# Concept: Data Integrity 
# Security+: Hash Functions, Integrity, One-way functions
# Self-directed cybersecurity lab Security+ SY0-701 aligned Cryptography fundamentals

import hashlib

# mental model: message → hash → signature → verification
# in real cryptography, private/public keys are mathematically related (PKI)
message="Version 2.1 Security Patch"  #string
private_key = "my_secret_key" #simulated encrypted private key
public_key="my_public_key" # conceptual placeholder for PKI structure (not used in current logic)

# function to grab the string from message, hash it and then results are returned outside function
def get_hash(message):
    # convert message string to bytes (required for hashing; strings are immutable)
    message_bytes = message.encode()

    # SHA-256 generates a hash object, then converted to hex string
    hash_object=hashlib.sha256(message_bytes)

    # convert into human readable hexadecimal
    hash_hex=hash_object.hexdigest()
    
    # return hash value to caller
    return(hash_hex)
    
result = get_hash(message) # runs the function and captures it
# message is hashed to hex format; matching hashes confirm integrity (not sender identity)

# function to simulate message + private key → signature
def sign_message(message, private_key):
    message_bytes=message.encode()
    hash_object=hashlib.sha256(message_bytes)
    hash_hex=hash_object.hexdigest()

    # simulated signature: hash + private key combined (not real cryptography)
    digital_signature=(hash_hex + private_key) # conceptually binds identity + integrity using string concatenation
    
    # sends the result/unique digital signature outside the function for use
    return digital_signature

# Mentally this is signed_message = digital_signature
signed_message=sign_message(message, private_key)

# Next step takes message + signature, recompute hash (slice message from private key) and verify that they match expected signature for authenticity.

def verify_message(message, signed_message, public_key):
    # recompute hash independently for verificationh
    verified_hash=get_hash(message)
    # extract original hash from signed message (first 64 chars of SHA-256 hex digest)
    extracted_hash=signed_message[:64]
    
    # compare hashes to determine validity (True = valid, False = invalid)
    return verified_hash == extracted_hash

#
if verify_message(message, signed_message, public_key):
    print("VALID: Message integrity and authenticity confirmed")
else:
    print("INVALID: Message may have been altered or spoofed")

# Flow resembles PKI however, simplified for my level of python and cryptgraphy skills.