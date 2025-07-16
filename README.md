## password-leak-check
A simple Python command-line tool that lets you check whether your password has been exposed in known data breaches using the Have I Been Pwned "Pwned Passwords" API. It follows the k-anonymity model to safeguard your privacy—only the first 5 characters of the SHA-1 hash are ever sent to the API, so your full password never leaves your machine

##🧪 Example usage:
python checkmypass.py password123 mySecret hello123
