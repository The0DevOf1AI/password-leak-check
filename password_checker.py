import requests  # For making HTTP requests
import hashlib   # For hashing the password
import sys       # To get command-line arguments



# Function to send a request to the Pwned Passwords API with the first 5 chars of SHA-1 hash
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        # Raise an error if the API call fails
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res


# Function to check how many times the password hash suffix was found in data breaches
def get_passwors_leaks_count(hashes_list, hash_to_check):
    for hashes in hashes_list:
        prt1, prt2 = hashes.split(":")  # Split into suffix and count
        if hash_to_check[5:] == prt1:   # Compare suffix of our hash with each returned one
            return int(prt2)            # Return how many times it's been seen
    return 0  # Return 0 if not found


# Function that hashes the password and checks if it was leaked
def pwned_api_checked(password):
    hashes_list = []  # List to store suffixes from the API
    # Hash the password using SHA-1 and convert to uppercase hexadecimal
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # Split the hash into prefix (first 5 chars) and suffix (remaining 35 chars)
    first5_char, tail = sha1password[:5], sha1password[5:]
    # Query the API using the prefix
    response = request_api_data(first5_char)
    # Split the response into lines and collect suffixes
    for hashes in response.text.splitlines():
        hashes_list.append(hashes)
    # Check if the suffix exists in the response
    return get_passwors_leaks_count(hashes_list, sha1password)


# Main function to handle all passwords passed from the command line
def main(args):
    for file in args:
        try:
            with open(str(file), 'r') as pass_file:
                content = pass_file.read()
                passwords = content.split(",")
                for password in passwords:
                    count = pwned_api_checked(password)  # Check each password
                    if count:
                        print(f'Your password: {password} has been found {count} times. You should change it!')
                    else:
                        print(f"Your password: {password} was NOT found. Carry on!")
                return 'done!'    
                
        except FileNotFoundError:
            print("Check your file path.")


# Run the script with command-line arguments (excluding the script name itself)
if __name__ == '__main__':
    main(sys.argv[1:])
