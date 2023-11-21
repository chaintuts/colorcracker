/* This file creates a database user for ColorCracker
* Change these values to your own and rename this file to "db_user.sql"
*
* Author: Josh McIntyre
*/

/* This block creates the user */
CREATE USER "ColorCrackerUser"@"localhost" IDENTIFIED BY "MyPassword";

/* This block grants all privileges on the database to the new user */
GRANT SELECT ON ColorCrackerDB.* TO "ColorCrackerUser"@"localhost";
FLUSH PRIVILEGES;

