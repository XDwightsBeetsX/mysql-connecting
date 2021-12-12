import mysql.connector as mysql
import sys

# ====================================================================== #
# Set these variables to test the MySQL Database Connection.             #
# Optionally, pass in the path to the 'creds.txt' file via command line  #
# ====================================================================== #
serverName = "localhost"
username = "root"
password = ""
database = "test"



# ====================================================================== #
# This program will try to make the connection                           #
#   - uses the mysql-connector-python package                            #
#     - https://github.com/mysql/mysql-connector-python                  #
# ====================================================================== #
if __name__ == "__main__":
    print("Running MySQL Connection Test...\n")

    # optionally, pass in a file with fields matching required credentials
    if len(sys.argv) > 1:
        print("Reading in Credentials from File...")
        print("Expected Filename is 'creds.txt'")
        print('Expected credential format is: cred=value, or cred="value"')
        
        credentialFileName = sys.argv[1].strip()
        gotSN, gotSP, gotUN, gotP = False, False, False, False
        with open(credentialFileName, 'r') as cred:
            creds = cred.readlines()
            for c in creds:
                line = c.split("=")
                val = str(line[1].strip().strip('"'))
                if line[0] == "server":
                    serverName = val
                    gotSN = True
                elif line[0] == "username":
                    username = val
                    gotSP = True
                elif line[0] == "password":
                    password = val
                    gotUN = True
                elif line[0] == "database":
                    database = val
                    gotP = True
            if not (gotSN and gotSP and gotUN and gotP):
                print("Could not find all credentials in file.")
                print("need: <server>, <username>, <password>, and <database>")
                print(f"got: {creds}")
                print("ending...")
                quit()
            else:
                print(f"Obtained credentials from {credentialFileName}\n")
    
    print("Attempting Connection with following credentials:")
    print(f"server:   {serverName}")
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"database: {database}\n")

    try:
        conn = mysql.connect(
            host=serverName,
            user=username,
            password=password,
            database=database)
        
        if conn.is_connected():
            print("Connection established.")

    except Exception as e:
        print("Encountered and error during connection:")
        print(e)
    