# Password Leak Checker (File-Based)

This Python script checks whether a list of passwords (stored in a file) have been exposed in known data breaches by querying the [Have I Been Pwned](https://haveibeenpwned.com/API/v3#PwnedPasswords) Pwned Passwords API.

It uses SHA-1 hashing and the k-Anonymity technique to ensure that your full password is never sent to the API, protecting your privacy.

---

## 🔧 Features

- Reads passwords from a `.txt` file (comma-separated).
- Checks each password against the Pwned Passwords API.
- Reports how many times each password has been found in data breaches.
- Secure: never transmits the full password or hash.

---

## 🧰 Requirements

- Python 3.x
- `requests` library

You can install the required dependency with:

```bash
pip install requests
```

## 📄 Input Format
Create a `.txt` file containing your passwords separated by commas.
Example:

123456,password123,mySecretPassword

## ▶️ Usage
Run the script from the command line, passing the file path as an argument:
```
python password_checker.py passwords.txt
```
## Sample output:
Your password: 123456 has been found 2345678 times. You should change it!.

Your password: mySecretPassword was NOT found. Carry on!.
