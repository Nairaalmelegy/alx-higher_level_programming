#!/usr/bin/python3
"""
Script lists all states from a database
"""
import MySQLdb
import sys


def main():
    # check if correct number of arg is provided
    if len(sys.argv) != 4:
        print("Usae: {} username password database".format(sys.argv[0]))
        return

    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # To connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, 
                         passwd=password, db=database)
    cursor = db.cursor()

    # SQL query execution
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
