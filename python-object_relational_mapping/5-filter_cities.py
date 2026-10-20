#!/usr/bin/env python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Fixed: Removed trailing comma and split string for PEP 8 compliance
    query = (
        "SELECT cities.id, cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (sys.argv[4],))
    results = cursor.fetchall()

    # Format output as comma-separated city names
    print(", ".join([row[1] for row in results]))
    cursor.close()
    db.close()

