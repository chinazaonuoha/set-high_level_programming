#!/usr/bin/env python3
"""This script lists all states from the database hbtn_0e_0_usa
where name matches the argument provided by the user."""
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
        "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC",
        (sys.argv[4],))

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the connection
    cursor.close()
    db.close()
