import sqlite3 , csv , sys
connection = sqlite3.connect("sample_travel_site.db")
cur = connection.cursor()

# Query-1
sql = ("update Flight_information set fare = 6500 where flight_id = '6E 292'")
cur.execute(sql)
print(cur.fetchall())

# Query-2
sql = ("select count(destination) as c , destination from Flight_Booking group by destination order by c DESC")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-3
sql = ("select first_name, customer_contact, customer_email, count(customer_id) as c from Flight_Booking natural join Customer group by customer_id order by c DESC")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-4
sql = ("select first_name, customer_contact, customer_email, customer_id from Customer where customer_id in (select customer_id from Flight_Booking where date_of_journey = '5/16/2020' and start_point = 'Jaipur' and destination = 'Mumbai')")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-5
sql = ("select count(destination) as c , destination from Bus_Booking group by destination order by c DESC")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-6
sql = ("select first_name, customer_contact, customer_email, count(customer_id) as c from Bus_Booking natural join Customer group by customer_id order by c DESC")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-7
sql = ("select first_name, customer_contact, customer_email, customer_id from Customer where customer_id in (select customer_id from Bus_Booking where date_of_journey = '2020/05/11' and start_point = 'Jaipur' and destination = 'Mumbai')")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-8
sql = ("update Bus_information set fare = 1200 where bus_id = '1'")
cur.execute(sql)
print(cur.fetchall())
print()


# Query-9
sql = ("update Room_Information set fare = 1200 where room_id = '001'")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-10
sql = ("select count(h.city) as c, h.city , h.hotel_name from Hotel h join Room_Booking r where h.hotel_name = r.hotel_name and h.company_id = r.company_id group by h.city order by c DESC")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-11
sql = ("select first_name, customer_contact, customer_email, count(customer_id) as c from Room_Booking natural join Customer group by customer_id order by c DESC")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-12
sql = ("select * from flights_view where start_point = 'Jaipur' and destination='Mumbai'")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-13
sql = ("select * from buses_view where start_point = 'Jaipur' and destination='Mumbai'")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-14
sql = ("select * from flights_view where start_point = 'Jaipur' and destination='Mumbai' and fare<4000")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-15
sql = ("select * from buses_view where start_point = 'Jaipur' and destination='Mumbai' and fare<1000")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-16
sql = ("select * from buses_view where start_point = 'Jaipur' and destination='Mumbai' order by departure_time")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-17
sql = ("select * from flights_view where start_point = 'Jaipur' and destination='Mumbai' and departure_time > time('now') order by departure_time")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-18
sql = ("select * from hotels_view where city='Panaji'")
cur.execute(sql)
print(cur.fetchall())
print()

# Query-19
sql = ("select * from hotels_view where hotel_name ='Hilton: Goa' order by fare")
cur.execute(sql)
l = cur.fetchall()
for out in l:
	print("entered")
	print (out)
	print()

# Query-20
sql = ("select * from hotels_view where hotel_name ='Hilton: Goa' and room_type='4 - Star Room'")
cur.execute(sql)
print(cur.fetchall())
for out in cur.fetchall():
	print (out)
	print()


sql = ("select time('now')")
cur.execute(sql)
print(cur.fetchall())


connection.commit()