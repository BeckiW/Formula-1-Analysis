import statistics, sys, sqlite3
import matplotlib.pyplot as plt


# Main Function
def main(argv):
	# Connect to database and setup the connection
	dbConnection = sqlite3.connect('formula1data.db')
	dbConnection.row_factory = sqlite3.Row

	# The SQL we want to run
	sql = """SELECT drivers.forename, drivers.surname, COUNT(*) as wins FROM results
			LEFT JOIN drivers ON results.driverId = drivers.driverId
			WHERE results.number = 1
			GROUP BY drivers.driverId
			ORDER BY wins DESC
			LIMIT 30
			"""

	# Run the SQL
	print("Sql:", sql)
	cursor = dbConnection.execute(sql)
	rows = cursor.fetchall()

	# Print Results
	print("== Results ==")

	for row in rows:
		print(row["forename"], row["surname"], row["wins"])

	# Prepare Data for Plotting
	xData = []		# x-values simply count up for each driver (0-N)
	xTicks = []		# Bit of a hack to show the labels in the middle of the bars
	yData = []		# y-values are the number of wins they had
	labels = []		# Label for the x-axis (driver name) to hide number
	count = 0

	for row in rows:
		xData.append(count)
		xTicks.append(count + 0.5)
		yData.append(row["wins"])
		labels.append(row["forename"] + " " + row["surname"])

		count = count + 1		

	# Plot the chart
	plt.bar(xData, yData)
	plt.xticks(xTicks, labels, rotation=-90)
	plt.tight_layout()
	plt.show()



# Call Main Function
if __name__ == "__main__":
    main(sys.argv)
