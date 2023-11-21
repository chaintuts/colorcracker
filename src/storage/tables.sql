/* This file creates a database and table for the ColorCracker application
*
* Author: Josh McIntyre
*/

/* This block creates the database */
CREATE DATABASE ColorCrackerDB;

/* This block creates related tables to store the simple rainbow table data */
USE ColorCrackerDB;

CREATE TABLE PwHashes
(
	Hash CHAR(64) NOT NULL,
	Password VARCHAR(64) NOT NULL,

	PRIMARY KEY (Hash)
);
