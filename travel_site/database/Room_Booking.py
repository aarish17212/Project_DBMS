import csv
import random
import datetime

infos = []
with open("Room_information.csv",'r') as info:
	info = csv.DictReader(info)
	for row in info:
		infos.append(row)

count = 0
end_count = 0
dates = {}
bookings = []
while(len(bookings)<60):
	
	with open("Hotel.csv",'r') as file:
		file = csv.reader(file)
		header = next(file)
		for row in file:
			hotel_name = row[0]
			company_id = row[1]
			no_of_rooms = row[5]
			count = end_count
			end_count += int(no_of_rooms)
			address = row[4]
			room_type = [0 for i in range(7)]
			rooms = {}
			for row in infos[count:end_count]:
				if(row['hotel_name']==hotel_name):
					room_type[int(row['roomType'][0])] += 1
					if row['roomType'][0] in rooms:
						arr = rooms[int(row['roomType'][0])]
						arr.append(row)
						rooms[int(row['roomType'][0])] = arr
					else:
						rooms[int(row['roomType'][0])] = [row]

			booked_rooms = random.randint(1,int(no_of_rooms))
			# print(booked_rooms)
			for booking in range(booked_rooms):

				customer = random.randint(1,100)
				day = 1
				duration = 2

				
				check = True
				booking = True
				if customer in dates:
					while(True):
						for time in dates[customer]:
							if (day > time + 2 or day+2 < time)==False:
								check = False
								break
						if(check):
							days = dates[customer]
							days.append(day)
							dates[customer] = days
							break

						else:
							day += 5
							if(day>31):
								booking=False
								break


				else:
					dates[customer] = [day]

				if(booking):
					start_date = datetime.datetime(2020,5,day)
					end_date = datetime.datetime(2020,5,day+duration)

					room = random.randint(1,6)
					room_id = 0
					no_of_guest = 0
					fare = 0

					if(room_type[room]>0):
						room_type[room]-=1
						room_choices = rooms[room]
						# print(len(room_choices))
						for choice in room_choices:
							room_id = choice['room_id']
							no_of_guest = random.randint(1,int(choice['capacity']))
							fare = choice['fare']
							room_choices.remove(choice)
							break

					else:
						for room in range(1,7):
							print("entered")
							if(room_type[room]>0):
								room_type[room]-=1
								room_choices = rooms[room]
								# print(room_choices)
								for choice in room_choices:
									# print(choice)
									room_id = choice['room_id']
									no_of_guest = random.randint(1,int(choice['capacity']))
									fare = choice['fare']
									room_choices.remove(choice)
									break

					if(room_id==0):
						booking = False

					if(booking):
						room = str(room) + " " + "-" + " " + "Star" + " " + "Room"
						print(room)
						bookings.append({'company_id':company_id, 'hotel_name':hotel_name,'address':address,'booking_id':len(bookings)+1,'customer_id':customer,
							'room_type':room,'check_in':start_date,'check_out':end_date,'no_of_guest':no_of_guest,'room_id':room_id, 'fare':fare})

				print(len(bookings))

				if(len(bookings)==60):
					break
			if(len(bookings)==60):
				break

with open("Room_Booking.csv",'w') as file:
	file = csv.DictWriter(file,fieldnames=['company_id','hotel_name','address','booking_id','customer_id','room_type',
		'check_in','check_out','no_of_guest','room_id','fare'])
	file.writeheader()
	file.writerows(bookings)


