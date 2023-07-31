#!/usr/bin/python3
"""Script to list all states from the hbtn_0e_0_usa database"""

import sys
import MySQLdb

def main():
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL connection details from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Execute the query to fetch all states in ascending order by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    # Fetch all the rows from the result
    rows = cursor.fetchall()

    # Display the results as they are in the example
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
