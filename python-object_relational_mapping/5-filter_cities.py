#!/usr/bin/python3
""" Write a script that takes in the name of a state as an argument and lists \
all cities of that state, using the database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    state_arg = sys.argv[4]
    cur = db.cursor()
    query = "SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities INNER JOIN \
    states ON cities.state_id = states.id WHERE \
    states.name = %s ORDER BY cities.id ASC;"
    cur.execute(query, (state_name,))
    result = cur.fetchone()
    if result[0]:
        print(result[0])
    cur.close()
    db.close()
