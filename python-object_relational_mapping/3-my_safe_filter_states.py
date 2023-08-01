#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the states \
table of hbtn_0e_0_usa where name matches the argument. But this time, write \
one that is safe from MySQL injections! """
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    state_arg = sys.argv[4]
    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s;"
    cur.execute(query, (state_arg,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
