#!/usr/bin/python3
"""Script to list all states with a name starting with 'N' from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL connection details from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Execute the query to fetch states starting with 'N' in ascending order by states.id
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")

    # Fetch all the rows from the result
    rows = cur.fetchall()

    # Display the results as they are in the example
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
