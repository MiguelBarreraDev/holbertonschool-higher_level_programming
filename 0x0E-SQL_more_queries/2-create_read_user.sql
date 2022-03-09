-- Commans to managment a database
/**
 * Query: Create the database hbtn_d_2 and the user user_0d_2
 * Privileges: SELECT
 * Password: user_0d_2_pwd
 * If the database or user already exists, your script should not fail
 */
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
ALTER USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* TO user_0d_2@localhost;
