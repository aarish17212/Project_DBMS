import sqlite3 , csv , sys
connection = sqlite3.connect("database.db")
cur = connection.cursor()

# Creating Indexes

sql = ("Create index trending_destination_1 on Flight_Booking(destination)")
cur.execute(sql)

sql = ("Create index trending_destination_2 on Bus_Booking(destination)")
cur.execute(sql)

sql = ("Create index room_quality on Room_Booking(room_type)")
cur.execute(sql)

sql = ("Create index trending_customer_1 on Flight_Booking(customer_id)")
cur.execute(sql)

sql = ("Create index trending_customer_2 on Bus_Booking(customer_id)")
cur.execute(sql)

sql = ("Create index trending_customer_3 on Room_Booking(customer_id)")
cur.execute(sql)

sql = ("Create index budget_1 on Flight_Information(fare)")
cur.execute(sql)

sql = ("Create index budget_2 on Bus_Information(fare)")
cur.execute(sql)

sql = ("Create index budget_3 on Room_Information(fare)")
cur.execute(sql)

sql = ("Create index time_1 on Flight_Information(departure_time)")
cur.execute(sql)

sql = ("Create index time_2 on Bus_Information(departure_time)")
cur.execute(sql)

sql = ("Create index trending_city on Hotel(city)")
cur.execute(sql)

sql = ("Create index start_1 on Flight_Information(start_point)")
cur.execute(sql)

sql = ("Create index start_2 on Bus_Information(start_point)")
cur.execute(sql)

sql = ("Create index end_1 on Flight_Information(destination)")
cur.execute(sql)

sql = ("Create index end_2 on Bus_Information(destination)")
cur.execute(sql)


sql = ("Create index room_quality on Room_Booking(room_type)")
cur.execute(sql)

sql = ("Create index trending_customer_3 on Room_Booking(customer_id)")
cur.execute(sql)

sql = ("Create index budget_3 on Room_Information(fare)")
cur.execute(sql)

sql = ("Create index trending_city on Hotel(city)")
cur.execute(sql)

sql = ("Create index book_date_1 on Flight_Booking(date_of_journey)")
cur.execute(sql)

sql = ("Create index book_date_2 on Bus_Booking(date_of_journey)")
cur.execute(sql)



# sql = ("select * from Flight_Booking where destination='New Delhi'")
# cur.execute(sql)

# print(len(cur.fetchall()))
# print(cur.fetchall())

# sql = ("select strftime('%d/%m/%Y',date(substr(date_of_journey, 7, 4) || '-' || substr(date_of_journey, 4, 2) || '-' || substr(date_of_journey, 1, 2))) from Flight_Booking")
# cur.execute(sql)

# print(cur.fetchall())

# sql = ("select strftime('%m','2020-10-09') as months")
# cur.execute(sql)
# print(cur.fetchall())


# sql = ("select substr(date_of_journey,6,7) from Flight_Booking")
# cur.execute(sql)
# print(cur.fetchall())

# sql = ("select julianday('now')-julianday(select convert(date,fb.date_of_journey)) as diff from Flight_Booking as fb")
# cur.execute(sql)

# print(cur.fetchall())

# sql = ("select date_of_journey from Flight_Booking")
# cur.execute(sql)

# print(cur.fetchall())


connection.commit()