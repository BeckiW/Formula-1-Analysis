import statistics
import sys
import sqlite3
import matplotlib.pyplot as plt


# Main Function
def main(argv):
    # Connect to database and setup the connection
    dbConnection = sqlite3.connect('formula1data.db')
    dbConnection.row_factory = sqlite3.Row

    # The SQL we want to run
    sql = """
    SELECT drivers.forename, drivers.surname, AVG(points) as points FROM results
	LEFT JOIN drivers ON results.driverId = drivers.driverId
    GROUP BY drivers.driverId
    ORDER BY points DESC
	LIMIT 30
    """

    # Run the SQL
    print("Sql:", sql)
    cursor = dbConnection.execute(sql)
    rows = cursor.fetchall()

    # Print Results
    print("== Results ==")

    for row in rows:
        print(row["forename"], row["surname"], row["points"])

        

# Call Main Function
if __name__ == "__main__":
    main(sys.argv)
