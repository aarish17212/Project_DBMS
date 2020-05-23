import sqlite3 , csv , sys
connection = sqlite3.connect("database.db")
cur = connection.cursor()

# # # Creating the Tables

# connection.execute('''CREATE TABLE Airline
# 			(airline_name varchar(20) not null unique,
#     company_id varchar(20) Primary key,
#     airline_password varchar(20) not null,
#     airline_email varchar(20) not null unique,
#     no_of_flights int,
#     head_office varchar(20));''')

# connection.execute('''CREATE TABLE Bus
# 			(bus_name varchar(20) not null unique,
#     company_id varchar(20) primary key,
#     bus_password varchar(20) not null,
#     bus_email varchar(20) not null unique,
#     no_of_buses int,
#     head_office varchar(20));''')


# connection.execute('''CREATE TABLE Hotel
# 			(hotel_name varchar(20), 
#     company_id varchar(20),
#     city varchar(20),
#     hotel_password varchar(20) not null,
#     hotel_email varchar(20) not null unique,
#     hotel_address varchar(20) not null,
#     no_of_rooms int,
#     parking_available bit(1) not null,
#     primary key(hotel_name,company_id));''')


# connection.execute('''CREATE TABLE Customer
# 			(first_name varchar(20) not null,
# 			last_name varchar(20) not null,
#     customer_id INTEGER primary key AUTOINCREMENT,
#     customer_password varchar(20) not null,
#     customer_email varchar(20) not null unique,
#     customer_contact char(10) not null unique,
#     customer_gender varchar(10) not null,
#     referal_code varchar(20));''')


# connection.execute('''CREATE TABLE Flight_Information
# 			(flight_id varchar(20) primary key,
# 	company_id varchar(20),
# 	start_point varchar(20) not null,
# 	destination varchar(20) not null,
# 	capacity int not null,
# 	no_of_haults int default 0,
# 	fare float(10) not null,
# 	arrival_time time not null,
# 	departure_time time not null,
# 	foreign key (company_id) references Airline);''')

# # class Flightseats(flight_id,date,capacity-)

# connection.execute('''CREATE TABLE Bus_Information
# 			(bus_id varchar(20) primary key,
# 	company_id varchar(20),
# 	start_point varchar(20) not null,
# 	destination varchar(20) not null,
# 	capacity int not null,
# 	no_of_haults int default 0,
# 	fare float(10) not null,
# 	arrival_time time not null,
# 	departure_time time not null,
# 	foreign key (company_id) references Bus);''')

# connection.execute('''CREATE TABLE Room_Information
# 			(room_type varchar(20) not null,
#     capacity int default 2,
#     fare float(10) not null,
#     company_id varchar(20),
#     room_id Integer primary key AUTOINCREMENT,
#     hotel_name varchar(20),
#     wifi bit(1) not null,
#     breakfast bit(1) not null,
#     hot_water bit(1) not null,
#     ac bit(1) not null,
#     heater bit(1) not null,
#     tv bit(1) not null,
#     foreign key (company_id,hotel_name) references Hotel);''')

# connection.execute('''CREATE TABLE Flight_Booking
# 			(flight_id varchar(20),
#     start_point varchar(20) not null,
#     destination varchar(20) not null,
#     booking_id INTEGER primary key AUTOINCREMENT,
#     customer_id varchar(20),
#     fare float(10) not null,
#     date_of_journey date not null,
#     no_of_seats int default 1,
#     foreign key (flight_id) references Flight_Information,
#     foreign key (customer_id) references Customer);''')

# connection.execute('''CREATE TABLE Bus_Booking
# 			(bus_id varchar(20),
#     start_point varchar(20) not null,
#     destination varchar (20) not null,
#     booking_id INTEGER primary key AUTOINCREMENT,
#     customer_id varchar(20),
#     date_of_journey date not null,
#     fare float(10) not null,
#     no_of_seats int default 1,
#     foreign key (bus_id) references Bus_Information,
#     foreign key(customer_id) references Customer);''')

# connection.execute('''CREATE TABLE Room_Booking
# 			(company_id varchar(20),
#     hotel_name varchar(20),
#     address varchar(50) not null,
#     booking_id INTEGER primary key AUTOINCREMENT,
#     customer_id varchar(20),
#     room_type varchar(20) not null,
#     check_in date not null,
#     check_out date not null,
#     no_of_guest int default 2,
#     room_id varchar(20),
# 	fare float(10) not null,
#     foreign key (company_id,hotel_name) references Hotel
#     foreign key(customer_id) references Customer
#     foreign key(room_id) references Room_Information);''')

# connection.execute('''CREATE TABLE Rate_Flight
#             (flight_id varchar(20) primary key,
#             ratingco
# sql = ("alter table Flight_Booking drop column rating")
# cur.execute(sql)
# sql = ("Alter table Flight_Booking add column rating int default null")
# cur.execute(sql)

sql = ("Alter table Bus_Booking add column rating int default 3")
cur.execute(sql)
sql = ("Alter table Room_Booking add column rating int default 3")
cur.execute(sql)


# connection.execute('''CREATE TABLE Rooms_left
#             (room_id varchar(20),
#             no_of_guest int not null,
#             check_in date not null,
#             check_out date not null,
#             primary key(room_id,check_in),
#             foreign key(room_id) references Room_Information);''')

# connection.execute('''CREATE TABLE Flight_seats
#             (flight_id varchar(20),
#             booking_date date not null,
#             seats int not null,
#             primary key(flight_id,booking_date),
#             foreign key(flight_id) references Flight_Information);''')


# connection.execute('''CREATE TABLE Bus_seats
#             (bus_id varchar(20),
#             booking_date date not null,
#             seats int not null,
#             primary key(bus_id,booking_date),
#             foreign key(bus_id) references Bus_Information);''')



# # # Populating the Tables

# # # Populating the Airlines Table

# with open ("./database/Airline.csv" , "rt") as Airline:
# 	data = csv.DictReader(Airline)
# 	to_db = [(i["Airline Name"],i["Company Id"],i["Password"],i["Email"],i["Number Of Flights"],i["Head Office"]) for i in data]

# connection.executemany("insert into Airline(airline_name,company_id,airline_password,airline_email,no_of_flights,head_office) values(?,?,?,?,?,?);",to_db)

# #Populating the Flight_Information table

# with open ("./database/Flight_information.csv" , "rt") as Flight_info:
# 	data = csv.DictReader(Flight_info)
# 	to_db = [(i["Flight Id"],i["Company Id"],i["Start_Point"],i["Destination"],i["Capacity"],i["Number of Haults"],i["Fare"],i["Arrival Time"],i["Departure Time"]) for i in data]

# connection.executemany("insert into Flight_information(flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) values(?,?,?,?,?,?,?,?,?);",to_db)
		
# #Popolating the Bus Table

# with open ("./database/Bus.csv" , "rt") as Bus:
# 	data = csv.DictReader(Bus)
# 	to_db = [(i["Bus Name"],i["Company Id"],i["Password"],i["Email"],i["Number Of Buses"],i["Head Office"]) for i in data]

# connection.executemany("insert into Bus(bus_name,company_id,bus_password,bus_email,no_of_buses,head_office) values(?,?,?,?,?,?);",to_db)


# # # Populating the Bus_Information Table

# with open ("./database/Bus_information.csv" , "rt") as Bus:
# 	data = csv.DictReader(Bus)
# 	# for i in data:
# 	# 	print(i)
# 	to_db = [(i["bus_id"],i["Company_id"],i["Start_point"],i["Destination"],i["Capacity"],i["No_of_Haults"],i["Fare"],i["Arrival_time"],i["Depart_time"]) for i in data]

# connection.executemany("insert into Bus_Information(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) values(?,?,?,?,?,?,?,?,?);",to_db)


# # Populating the Hotel Table

# with open ("./database/Hotel Info.csv" , "rt") as Hotel:
# 	data = csv.DictReader(Hotel)
# 	to_db = [(i["Hotel_name"],i["Company_id"],i["City"],i["Password"],i["Email"],i["Address"],i["No_of_rooms"],i["Parking"]) for i in data]

# connection.executemany("insert into Hotel(hotel_name,company_id,city,hotel_password,hotel_email,hotel_address,no_of_rooms,parking_available) values(?,?,?,?,?,?,?,?);",to_db)


# # # #Populating the Room_Information Table

# with open ("./database/Room_Infor.csv" , "rt") as Hotel:
# 	data = csv.DictReader(Hotel)
# 	to_db = [(i["room_type"],i["capacity"],i["fare"],i["company_id"],i["room_id"],i["hotel_name"],i["Wifi"],i["Breakfast"],i["AC"],i["TV"],i["Hot_water"],i["Heater"]) for i in data]

# connection.executemany("insert into Room_Information(room_type,capacity,fare,company_id,room_id,hotel_name,wifi,breakfast,ac,tv,heater,hot_water) values(?,?,?,?,?,?,?,?,?,?,?,?);",to_db)

# #Populating the Customer Table

# with open ("./database/Customer.csv" , "rt") as Customer:
# 	data = csv.DictReader(Customer)
# 	to_db = [(i["first_name"],i["last_name"],i["Customer_id"],i["Password"],i["email"],i["mobile_number"],i["gender"],i["Referral_code"]) for i in data]
	
# connection.executemany("insert into Customer(first_name,last_name,customer_id,customer_password,customer_email,customer_contact,customer_gender,referal_code) values(?,?,?,?,?,?,?,?);",to_db)


# # Populating the Flight_Booking Table


# with open ("./database/Flight_Booking.csv" , "rt") as booking:
# 	data = csv.DictReader(booking)
# 	to_db = [(i["Flight Id"],i["Start Point"],i["Destination"],i["Booking Id"],i["Customer Id"],i["Fare"],i["Date"]) for i in data]

# connection.executemany("insert into Flight_Booking(flight_id,start_point,destination,booking_id,customer_id,fare,date_of_journey) values(?,?,?,?,?,?,?);",to_db)

# #Populating the Bus_Booking Table

# with open ("./database/Bus_Booking.csv" , "rt") as booking:
# 	data = csv.DictReader(booking)
# 	to_db = [(i["Bus Id"],i["Start Point"],i["Destination"],i["Booking Id"],i["Customer Id"],i["Date Of Journey"],i["Fare"]) for i in data]

# connection.executemany("insert into Bus_Booking(bus_id,start_point,destination,booking_id,customer_id,date_of_journey,fare) values(?,?,?,?,?,?,?);",to_db)

# #Populating the Room_Booking Table

# with open ("./database/Room_Booking.csv" , "rt") as booking:
# 	data = csv.DictReader(booking)
# 	to_db = [(i["company_id"],i["hotel_name"],i["address"],i["booking_id"],i["customer_id"],i["fare"],i["room_type"],i["check_in"],i["check_out"],i["no_of_guest"],i["room_id"]) for i in data]

# connection.executemany("insert into Room_Booking(company_id,hotel_name,address,booking_id,customer_id,fare,room_type,check_in,check_out,no_of_guest,room_id) values(?,?,?,?,?,?,?,?,?,?,?);",to_db)
# # cur.execute("select * from Airline")
# # airlines = cur.fetchall()
# # for row in airlines:
# # 	print(row)

connection.commit()

