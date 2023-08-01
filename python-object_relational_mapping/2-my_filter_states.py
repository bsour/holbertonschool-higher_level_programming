#!/usr/bin/python3
""" script that takes an argument and dsiplays all values in states table """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         state_name=sys.argv[4])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER \
    BY id ASC;".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
