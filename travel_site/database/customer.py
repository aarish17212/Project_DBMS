import csv
import random
store = []
def generate_contact():
	start = 10**(9-1)
	end = 10**(9) - 1
	num = random.randint(start,end)
	if(num not in store):
		store.append(num)
		return num
	else:
		generate_contact()

new_rows = []
with open("Customer.csv",'r') as file:
	file = csv.reader(file)
	header = next(file)
	for row in file:
		new_rows.append(row)
		new_rows[-1].append(str(9)+str(generate_contact()))

with open("Customer_1.csv",'w') as file:
	file = csv.writer(file)
	file.writerow(header)
	file.writerows(new_rows)
