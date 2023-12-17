#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    t = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    x = t.cursor()
    x.execute("SELECT * FROM states")
    l = x.fetchall()
    for c in l:
        print(c)
    x.close()
    t.close()
