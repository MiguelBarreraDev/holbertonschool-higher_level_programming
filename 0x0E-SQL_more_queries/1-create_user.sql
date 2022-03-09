-- Commans to managment a database
/**
 * Query: Create the MySQL server user user_0d_1
 * Privileges: all
 * Password: user_0d_1_pwd
 * if the user already exists, your script should not fail
 */
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
