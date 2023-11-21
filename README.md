## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* ColorCracker is a simple rainbow table generation and search tool

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make load
Load the database
* make clean
Clean the build and data directories

### Features
* Generate hashes using a specified wordlist of passwords
* Load hashes and passwords into a MySQL database
* Search the database given a specified password hash
* Useful for unsalted passwords using standard cryptographic hashes

### Requirements
* Requires Python and MySQL

### Platforms
* Windows
* Linux
* MacOSX

## Usage
____________

### Configuration
* Configure database users and authentication in files `auth.py` and `db_user.sql`
* Run `make load` to configure initial database

### Command Line - Generate password hash database
* Run `make` and run `python3 colorcracker.py --load <wordlist_filename>` to generate hashes and load into the database

### Command Line - Search password hash database
* Run `python3 colorcracker.py --search <password_hash>`
* If the tool finds a password, it will print the password and password hash to the command line
* Otherwise, it will print that the password cannot be found
