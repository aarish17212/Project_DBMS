import csv
import random
new_rows = []

with open("Flight_information.csv",'r') as file:
	file = csv.reader(file)
	header = next(file)

	for row in file:
		
		new_rows.append(row)
		new_rows[-1].append(random.randint(1800,6800))



with open("Flight_information_1.csv",'w') as file:
	file = csv.writer(file)
	file.writerows(new_rows)

