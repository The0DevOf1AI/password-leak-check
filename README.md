# Password Leak Checker

This Python script checks if a given password has been exposed in known data breaches by querying the [Have I Been Pwned (HIBP) Pwned Passwords API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

It uses the k-Anonymity technique by sending only the first 5 characters of the SHA-1 hash of the password to the API, protecting the full password hash and maintaining user privacy.

---

## Features

- Securely checks if a password has been leaked without sending the full password or full hash.
- Uses SHA-1 hashing and k-Anonymity prefix search.
- Supports checking multiple passwords passed as command-line arguments.
- Reports how many times each password was found in data breaches.

---

## Requirements

- Python 3.x
- `requests` library

Install dependencies via pip if needed:

```bash
pip install requests
