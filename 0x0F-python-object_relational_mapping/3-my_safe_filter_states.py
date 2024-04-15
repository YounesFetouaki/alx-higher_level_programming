#!/usr/bin/python3

""" Module that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    """ Connection to a MySQL server """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    """ To obtain a Cursor object """
    cur = db.cursor()
    """ Executing queries """
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))
    """ Obtaining query results """
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    """ Close cursor """
    cur.close()
    """ Close connection """
    db.close()
