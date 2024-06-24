#!/usr/bin/python3
"""  Lists all regions from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                    passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    result_set = cursor.fetchall()
    for data_row in result_set:
        print(data_row)
    cursor.close()
    db_connection.close()
