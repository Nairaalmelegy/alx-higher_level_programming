#!/usr/bin/python3
"""
Script lists all states with name starting with (upper N)
from a database
"""


import sys
import MySQLdb


def main():

    # check arg in command line
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, 
                         passwd=password, db=database)
    cursor = db.cursor()

    #SQL query execution
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
