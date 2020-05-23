import csv
new_rows = []
check=0
with open("Flight_Booking.csv",'r') as file:
	file = csv.reader(file)
	header = next(file)
	for row in file:
		# print(check)
		new_rows.append(row)
		with open("Flight_information.csv",'r') as file2:
			file2 = csv.reader(file2)
			header2 = next(file2)
			for row2 in file2:
				
				# print(row[1],row2[0])
				# print(type(row[1]),type(row2[0]))
				if(str(row[1])==str(row2[0])):
					# print(-2)
					new_rows[-1].append(row2[-1])
					# print(new_rows[-1])
					# check=1
					break
				


with open("Flight_Booking_1.csv",'w') as file:
	file = csv.writer(file)
	file.writerow(header)
	file.writerows(new_rows)
