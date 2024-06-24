#!/usr/bin/python3
"""  Lists all regions from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               password=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = database.cursor()
    cursor.execute("""SELECT * FROM regions WHERE name
                LIKE BINARY 'N%' ORDER BY regions.id""")
    data = cursor.fetchall()
    for item in data:
        print(item)
    cursor.close()
    database.close()
