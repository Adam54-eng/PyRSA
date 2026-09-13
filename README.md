# 🔐 PyRSA

> A lightweight RSA cryptography library written entirely in pure Python.

PyRSA is an educational implementation of the **RSA public-key cryptosystem**. It demonstrates how RSA generates public and private keys using prime numbers, Euler's totient, modular inverses, and modular exponentiation — all without external dependencies.

---

## Features

* 🔑 Random prime number generation
* 🛡️ RSA public & private key generation
* 🔢 Automatic encryption key (`e`) generation
* 🔐 Automatic decryption key (`d`) generation
* ⚡ Fast modular exponentiation
* 📦 Pure Python (0 dependencies)
* 🎓 Designed for learning cryptography

---

# What is RSA?

RSA is one of the most widely used **public-key encryption** algorithms.

Unlike symmetric encryption, RSA uses **two different keys**:

* **Public Key** → Used to encrypt data.
* **Private Key** → Used to decrypt data.

The public key can safely be shared with anyone, while the private key must always remain secret.

### How RSA generates keys

1. Choose two prime numbers **p** and **q**.
2. Compute `n = p × q`.
3. Compute Euler's totient `φ = (p − 1)(q − 1)`.
4. Choose an integer `e` that is coprime with `φ`.
5. Compute the modular inverse `d`.

The resulting keys are:

* **Public Key:** `(e, n)`
* **Private Key:** `(d, n)`

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/PyRSA.git
```

Import the library:

```python
from pyrsa import RSAKey
```

**Requirements**

* Python 3.10+
* No external libraries

---

# Quick Start

```python
from pyrsa import RSAKey

rsa = RSAKey(100, 500)

rsa.generate_encryption_key()
rsa.generate_decryption_key()

message = 42

cipher = rsa.modular_pow(rsa.e, message)
plain = rsa.modular_pow(rsa.d, cipher)

print("Encrypted:", cipher)
print("Decrypted:", plain)
```

Output:

```text
Encrypted: 6932
Decrypted: 42
```

---

# API Reference

## Create a key pair

```python
rsa = RSAKey(100, 500)
```

The constructor randomly selects two different prime numbers within the given range.

## Generate the public key

```python
e = rsa.generate_encryption_key()
```

Generates a valid encryption exponent `e` such that:

* `2 ≤ e < φ`
* `gcd(e, φ) = 1`

## Generate the private key

```python
d = rsa.generate_decryption_key()
```

Computes the modular inverse of `e`.

## Encrypt

```python
cipher = rsa.modular_pow(rsa.e, message)
```

## Decrypt

```python
message = rsa.modular_pow(rsa.d, cipher)
```

---

# Example

```python
from pyrsa import RSAKey

rsa = RSAKey(50, 200)

rsa.generate_encryption_key()
rsa.generate_decryption_key()

text = 123

encrypted = rsa.modular_pow(rsa.e, text)
decrypted = rsa.modular_pow(rsa.d, encrypted)

print(f"Original : {text}")
print(f"Encrypted: {encrypted}")
print(f"Recovered: {decrypted}")
```

---

# Project Structure

```text
PyRSA/
│
├── pyrsa/
│   ├── __init__.py
│   └── rsa.py
│
├── examples/
│   └── basic.py
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# Educational Purpose

PyRSA is intentionally simple and readable. It is designed to help students understand:

* Prime number generation
* Euler's Totient Function
* Greatest Common Divisor (GCD)
* Modular inverses
* Modular exponentiation
* RSA key generation

> **Note:** This implementation is educational and is **not intended for real-world security**. Modern RSA uses cryptographically secure random number generators and keys of 2048 bits or larger.

---

# License

Released under the **MIT License**.
