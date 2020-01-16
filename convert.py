#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable called `polls`
with open('input.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	polls = [dict(row) for row in rows] # Convert OrderedDict to regular dict

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"
with open('output.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['date', 'approve'])

	# 3. Loop through each row of `polls` 
	for p in polls:

		enddate = p['enddate']
		approve = p['approve']

		# 4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"
		python_enddate = datetime.datetime.strptime(enddate, "%m/%d/%Y")
		new_format_enddate = python_enddate.strftime("%-d-%b-%y")

		# 5. write a new row of data with the transformed date and value for "approve" 
		writer.writerow([new_format_enddate, approve])
	# by Dhrumil and Sultan