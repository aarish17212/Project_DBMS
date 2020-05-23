import sqlite3
connection = sqlite3.connect("database.db")
cur = connection.cursor()

# SQL Queries for triggers.
CREATE trigger inc_flights AFTER INSERT ON Flight_Information
BEGIN
UPDATE Airline set no_of_flights  = no_of_flights + 1 where company_id = new.company_id;
END;

CREATE trigger inc_buses AFTER INSERT ON Bus_Information
BEGIN
UPDATE Bus set no_of_buses  = no_of_buses + 1 where company_id = new.company_id;
END;

CREATE TRIGGER inc_rooms AFTER INSERT ON Room_Information
BEGIN 
UPDATE Hotel set no_of_rooms = no_of_rooms + 1 where company_id = new.company_id and hotel_name = new.hotel_name; 
END;

CREATE TRIGGER dec_flights AFTER INSERT ON Flight_Booking
BEGIN 
UPDATE Flight_seats set seats = seats-new.no_of_seats where flight_id = new.flight_id and booking_date = new.date_of_journey; 
END;

CREATE TRIGGER dec_buses AFTER INSERT ON Bus_Booking
BEGIN 
UPDATE Bus_seats set seats = seats-new.no_of_seats where bus_id = new.bus_id and booking_date = new.date_of_journey; 
END;

CREATE TRIGGER rem_buses AFTER delete ON Bus_Information BEGIN UPDATE Bus set no_of_buses = no_of_buses - 1 where company_id = old.company_id; END

CREATE TRIGGER rem_flights AFTER delete ON Flight_Information BEGIN UPDATE Airline set no_of_flights = no_of_flights - 1 where company_id = old.company_id; END

CREATE TRIGGER rem_rooms AFTER delete ON Room_Information BEGIN UPDATE Hotel set no_of_rooms = no_of_rooms - 1 where company_id = old.company_id; END

