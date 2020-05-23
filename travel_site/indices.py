import sqlite3 , csv , sys
connection = sqlite3.connect("database.db")
cur = connection.cursor()


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