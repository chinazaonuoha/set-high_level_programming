#!/usr/bin/env python3
"""This script lists all states with a name starting
with N from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cursor = db.cursor()

    # Execute the query
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the connection
    cursor.close()
    db.close()
