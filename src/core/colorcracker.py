# This file contains the main entry point for the password hash generator
#
# Author: Josh McIntyre
#
import argparse

import hashgen
import loaddb
import searchdb

# The main entry point for the program
def main():

    parser = argparse.ArgumentParser(description="Load and search a simple rainbow table of password hashes")
    parser.add_argument("--load", type=str, help="Generate and load hashes from the specified wordlist filename")
    parser.add_argument("--search", type=str, help="Search for the specified password hash in an existing database")
    args = parser.parse_args()

    if args.load:
        hasher = hashgen.PasswordHasher(args.load)
        loader = loaddb.HashLoader()
    
        print(f"Total number of passwords in wordlist: {hasher.num_passwords}")
        for password, password_hash in hasher.get_password():
            print(f"Generated hash for {password}: {password_hash}")
            loader.load_hash(password_hash, password)
    
    if args.search:
        searcher = searchdb.HashSearcher()
        result = searcher.search_hash(args.search)
        if result:
            password_hash, password = result
            print(f"Found password {password} for hash {password_hash}")
        else:
            print("No password found for hash {args.search}")

if __name__ == "__main__":
    main()