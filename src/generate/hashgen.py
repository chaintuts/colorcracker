# This file contains code for generating password hashes from an initial wordlist
#
# Author: Josh McIntyre
#
import hashlib

from enum import Enum

# Constants
class SupportedHashes(Enum):

    SHA256 = hashlib.sha256
    SHA1 = hashlib.sha1
    MD5 = hashlib.md5

# Define a class for handling wordlists
class PasswordHasher:

    # Get initial information about the wordlist
    def __init__(self, wordlist_filename, hashing_algorithm=SupportedHashes.SHA256):
        
        self.hashing_algorithm = hashing_algorithm
        self.wordlist_filename = wordlist_filename
        with open(self.wordlist_filename) as f:
            self.num_passwords = sum(1 for _ in f)
            
    # Return an iterator for fetching each password line,
    # stripping out whitespace, 
    # then hashing with the specified algorithm
    # This generator returns a tuple with the raw password and password hash
    def get_password(self):

        with open(self.wordlist_filename) as f:
 
            for password_line in f:
                password = password_line.strip()
                hasher = self.hashing_algorithm.value()
                hasher.update(password.encode())

                yield (password, hasher.hexdigest())

