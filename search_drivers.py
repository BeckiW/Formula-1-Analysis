import statistics, sys, sqlite3
import matplotlib.pyplot as plt


# Main Function
def main(argv):
	if len(argv) < 2:
		print("Usage: python3 search_drivers.py SEARCH")
		exit()

	keyword = argv[1]

	dbConnection = sqlite3.connect('formula1data.db')
	dbConnection.row_factory = sqlite3.Row

	sql = "SELECT * FROM drivers WHERE (forename LIKE '%%%s%%') OR (surname LIKE '%%%s%%') ORDER BY forename" % (keyword, keyword)
	print("Sql:", sql)

	cursor = dbConnection.execute(sql)
	result = cursor.fetchall()

	print("== Results ==")

	for row in result:
		print(row["forename"], row["surname"])


# Call Main Function
if __name__ == "__main__":
    main(sys.argv)
