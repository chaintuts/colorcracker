# This file contains a make script for the ColorCracker application
#
# Author: Josh McIntyre
#

# This block defines makefile variables
SRC_FILES=src/core/*.py src/generate/*.py src/auth/*.py src/search/*.py
SQL_FILES=src/storage/tables.sql src/storage/db_user.sql
RES_FILES=res/*.txt

BUILD_DIR=bin/colorcracker
DATA_DIR=bin/data
DATA_SCRIPT=database.sql

DB=mysql
FLAGS=-u root -p --local-infile=1

# This rule builds the application
build: $(SRC_FILES) $(RES_FILES)
	mkdir -p $(BUILD_DIR)
	cp $(SRC_FILES) $(RES_FILES) $(BUILD_DIR)

# This rule loads the database
load: $(SQL_FILES) $(CSV_FILES)
	mkdir -p $(DATA_DIR)
	cat $(SQL_FILES) > $(DATA_DIR)/$(DATA_SCRIPT)
	cd $(DATA_DIR); \
		$(DB) $(FLAGS) < $(DATA_SCRIPT)

# This rule cleans the build and data directories
clean: $(BUILD_DIR) $(DATA_DIR)
	rm $(BUILD_DIR)/* $(DATA_DIR)/*
	rmdir $(BUILD_DIR) $(DATA_DIR) 
