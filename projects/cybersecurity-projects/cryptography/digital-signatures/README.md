# Cryptography Lab 1: SHA-256 Hashing and Digital Signature (Security+ Simulation)

A self-directed cybersecurity lab that demonstrates core cryptography concepts including SHA-256 hashing, digital signature creation, and basic verification logic. This project was built as part of my Security+ SY0-701 exam studies to reinforce understanding of data integrity and authentication concepts using Python.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates fundamental cryptography concepts in Python using a simplified simulation of hashing and digital signatures.

It focuses on Security+ SY0-701 concepts including:

- Hash functions (SHA-256)
- Data integrity
- One-way functions
- Digital signature concepts (simplified model)
- Verification logic (trust decision via boolean output)

The goal of this project is to build a clear mental model of how message integrity and authenticity are verified in a secure system.

### Subsection

### Conceptual Flow

Message → SHA-256 Hash → Digital Signature (simulated) → Verification → VALID / INVALID result

This is a simplified educational model and does not use real cryptographic key exchange.

## Features

- SHA-256 hashing using Python `hashlib`
- Custom function for reusable hashing logic
- Simulated digital signature creation using concatenation of hash + private key
- Verification function that independently recomputes hash
- Boolean-based trust decision (True = valid, False = invalid)
- Clear separation of signing vs verification logic

## Installation

To run this project, ensure you have Python installed.

No external libraries are required beyond the Python standard library.

```bash
python sha256-hash-lab.py
```

## Usage

Run the script to see:

- Original message
- SHA-256 hash output
- Simulated digital signature
- Verification result (VALID / INVALID)

### Example output:

VALID: Message integrity and authenticity confirmed

You can modify the `message` variable to test how changes affect the verification result.

## Contributing

This is a personal learning project for my Security+ and Python practice.

This project is not currently accepting external contributions.

## Future Improvements

- Tamper detection demo (message modification test)
- Expanded cryptography simulations
- Improved PKI-style structure modeling
- Visualization of signing vs verification flow

## License

This project is for educational purposes only.

```

```
