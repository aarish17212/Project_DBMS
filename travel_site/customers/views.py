from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic.edit import FormView, FormMixin
from .forms import search_form,search_flights,bookflight, search_buses, bookbus, search_hotels, bookroom,rating
from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import var
dates = []
ind = []
oud = []
import smtplib
import announcements

hotels = {}
buses = {}
flights = {}

class flight:

	def __init__(self,details):
		self.flight_id = details[0]
		self.airline_name = details[1]
		self.fare = details[2]
		self.capacity = details[3]
		self.departure_time = details[4]
		self.arrival_time = details[5]
		self.no_of_haults = details[6]

class hotel:

	def __init__(self,details):

		self.hotel_name = details[0]
		self.city = details[1]
		self.hotel_address = details[2]
		self.parking_available = details[3]
		self.room_type = details[4]
		self.fare = details[5]
		self.capacity = details[6]
		self.wifi = details[7]
		self.breakfast = details[8]
		self.hot_water = details[9]
		self.ac = details[10]
		self.tv = details[11]
		self.heater = details[12]
		self.room_id = details[13]

class booking1:

	def __init__(self,details):

		self.start_point = details[0]
		self.destination = details[1]
		self.fare = details[2]
		self.date = details[3]
		self.id = details[4]


class booking2:

	def __init__(self,details):

		self.hotel_name = details[0]
		self.check_in = details[1]
		self.check_out = details[2]
		self.fare = details[3]
		self.room_id = details[4]

def home(request):
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	print("Entered")
	form = search_form()
	print(var.login)
	flight_des = [None,None,None]
	flight_start = [None,None,None]
	bus_des = [None,None,None]
	bus_start = [None,None,None]
	if(var.login):
		sql = ("select count(destination) as c , destination from Flight_Booking where customer_id = ? group by destination order by c DESC")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		for i in range(min(3,len(result))):
			flight_des[i] = result[i][1]

		print(flight_des)
			
		sql = ("select count(start_point) as c , start_point from Flight_Booking where customer_id = ? group by start_point order by c DESC")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		for i in range(min(3,len(result))):
			flight_start[i] = result[i][1]
			
		sql = ("select count(destination) as c , destination from Bus_Booking where customer_id = ? group by destination order by c DESC")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		for i in range(min(3,len(result))):
			bus_des[i] = result[i][1]
			
		sql = ("select count(start_point) as c , start_point from Bus_Booking where customer_id = ? group by start_point order by c DESC")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		for i in range(min(3,len(result))):
			bus_start[i] = result[i][1]
		
	print(var.login)

	for a in announcements.a:
		print(a)
	return render(request,'customers/index.html',{'form':form,'searches':["flights","buses","hotels","Cart"],'login':var.login, 'flight_des1':flight_des[0],'flight_des2':flight_des[1],'flight_des3':flight_des[2],'flight_start1':flight_start[0],'flight_start2':flight_start[1],'flight_start3':flight_start[2], 'bus_des1':bus_des[0],'bus_des2':bus_des[1],'bus_des3':bus_des[2],'bus_start1':bus_start[0],'bus_start2':bus_start[1],'bus_start3':bus_start[2],'a':announcements.a})

def search_flight(request):
	global dates
	dates = []
	print("Entered--1")
	form = search_flights()

	if(request.method == 'POST'):
		date = request.POST.get('date_year')+"-"+request.POST.get('date_month')+"-"+request.POST.get("date_day")
		dates.append(date)
		start_point = request.POST.get('start_point')
		destination = request.POST.get('destination')
		max_budget = request.POST.get('max_budget')
		max_time_in_hrs = request.POST.get('max_time_in_hrs')

		if(max_budget==""):
			max_budget = 100000
		if(max_time_in_hrs==""):
			max_time_in_hrs = 100

		return redirect('customer_flights',start_point,destination,max_budget,max_time_in_hrs)


	else:
		form.fields['date'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
				empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020',),months= {5: ('May')})
		return render(request,'customers/searchflight.html',{'form':form,'login':var.login})


def search_bus(request):
	global dates
	dates = []
	print("Entered--1")

	form = search_buses()

	if(request.method == 'POST'):
		date = request.POST.get('date_year')+"-"+request.POST.get('date_month')+"-"+request.POST.get("date_day")
		dates.append(date)
		start_point = request.POST.get('start_point')
		destination = request.POST.get('destination')
		max_budget = request.POST.get('max_budget')
		max_time_in_hrs = request.POST.get('max_time_in_hrs')

		if(max_budget==""):
			max_budget = 100000
		if(max_time_in_hrs==""):
			max_time_in_hrs = 100

		return redirect('customer_buses',start_point,destination,max_budget,max_time_in_hrs)


	else:
		form.fields['date'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
				empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020',),months= {5: ('May')})

		return render(request,'customers/searchbus.html',{'form':form,'login':var.login})


def search_hotel(request):
	print("Entered--1")
	global ind,oud
	ind = []
	oud = []
	form = search_hotels()

	if(request.method == 'POST'):
		check_in = request.POST.get('check_in_year')+"-"+request.POST.get('check_in_month')+"-"+request.POST.get("check_in_day")
		check_out = request.POST.get('check_out_year')+"-"+request.POST.get('check_out_month')+"-"+request.POST.get("check_out_day")
		ind.append(check_in)
		oud.append(check_out)
		city = request.POST.get('city')
		max_budget = request.POST.get('max_budget')
		room_type = request.POST.get('room')
		parking_available = request.POST.get('parking')

		if(max_budget==""):
			max_budget = 100000

		return redirect('customer_hotels',city,max_budget,room_type,parking_available)


	else:
		form.fields['check_in'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'),months= {5: ('May')})
		form.fields['check_out'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'),months= {5: ('May')})
		return render(request,'customers/searchhotel.html',{'form':form,'login':var.login})


# def addbus(request,id):
# 	global hotels,buses,flights,dates

# 	if(request.method=="POST"):
		
# 		no_of_seats = request.POST.get('no_of_seats')
# 		buses[id] = [no_of_seats,dates[-1]]



# 	else:

# 		form = bookbus()
# 		sql = ("select sum(no_of_seats) from Bus_Booking where bus_id=? and date_of_journey=?")
# 		cur.execute(sql,(id,dates[-1],))
# 		res = cur.fetchall()
# 		print(res)
# 		sql = ("select capacity from Bus_Information where bus_id=?")
# 		cur.execute(sql,(id,))
# 		capacity = cur.fetchall()

# 		print(res[0][0])
# 		if(res[0][0] is not  None):
# 			form.fields['no_of_seats'] = forms.IntegerField(max_value=capacity[0][0]-res[0][0])
# 		else:
# 			form.fields['no_of_seats'] = forms.IntegerField(max_value=capacity[0][0])

# 		return render(request,'customers/busbooking.html',{'form':form,'login':var.login})


# def cart(request):
# 	global buses,hotels,flights

def rf(request,id):
	print("Her1")
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
	if(var.login):
		if(request.method=="POST"):
			rate = request.POST.get('rate')
			print(rate)
			messages.success(request,"Your Valuable feedback has been recorded")

			sql = ("update Flight_Booking set rating = ? where booking_id=? and customer_id=?")
			cur.execute(sql,(int(rate),id,var.login_id,))
			connection.commit()
			return redirect('fbookings')

		else:
			form = rating()
			return render(request,'customers/rate.html',{'form':form,'login':var.login})

	else:
		return redirect('login')


def rb(request,id):
	print("Here")
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
	if(var.login):
		if(request.method=="POST"):
			rate = request.POST.get('rate')
			print(rate)
			messages.success(request,"Your Valuable feedback has been recorded")

			sql = ("update Bus_Booking set rating = ? where booking_id=? and customer_id=?")
			cur.execute(sql,(int(rate),id,var.login_id,))
			connection.commit()
			return redirect('bbookings')

		else:
			form = rating()
			return render(request,'customers/rate.html',{'form':form,'login':var.login})

	else:
		return redirect('login')

def rh(request,id):
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
	if(var.login):
		if(request.method=="POST"):
			rate = request.POST.get('rate')
			print(rate)
			messages.success(request,"Your Valuable feedback has been recorded")

			sql = ("update Room_Booking set rating = ? where booking_id=? and customer_id=?")
			cur.execute(sql,(int(rate),id,var.login_id,))
			connection.commit()
			return redirect('hbookings')

		else:
			form = rating()
			return render(request,'customers/rate.html',{'form':form,'login':var.login})

	else:
		return redirect('login')

def fbookings(request):
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):

		

		hb = []
		bb = []
		fb = []

		sql = ("select julianday('now') - julianday(?)")
		cur.execute(sql,('2020-05-11',))
		print(cur.fetchall()[0][0])

		sql1 = ("select start_point,destination,fare,date_of_journey,booking_id from Flight_Booking where customer_id=?")
		cur.execute(sql1,(var.login_id,))
		r1 = cur.fetchall()

		for details in r1:
			fb.append(booking1(details))

		# sql2 = ("select start_point,destination,fare,date_of_journey,bus_id from Bus_Booking where customer_id=?")
		# cur.execute(sql2,(var.login_id,))
		# r1 = cur.fetchall()

		# for details in r1:
		# 	bb.append(booking1(details))

		# sql3 = ("select hotel_name,check_in,check_out,fare,room_id from Room_Booking where customer_id=?")
		# cur.execute(sql3,(var.login_id,))
		# r1 = cur.fetchall()

		# for details in r1:
		# 	hb.append(booking2(details))

		
		form = rating()
		return render(request,'customers/mybookings.html',{'form':form,'fb':fb,'login':var.login})

	else:
		messages.error(request,"Log In to see your bookings")
		return redirect('customer_home')


def bbookings(request):
	print("heree2")
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):

		

		hb = []
		bb = []
		fb = []

		sql = ("select julianday('now') - julianday(?)")
		cur.execute(sql,('2020-05-11',))
		print(cur.fetchall()[0][0])

		sql2 = ("select start_point,destination,fare,date_of_journey,booking_id from Bus_Booking where customer_id=?")
		cur.execute(sql2,(var.login_id,))
		r1 = cur.fetchall()

		for details in r1:
			bb.append(booking1(details))

		# sql2 = ("select start_point,destination,fare,date_of_journey,bus_id from Bus_Booking where customer_id=?")
		# cur.execute(sql2,(var.login_id,))
		# r1 = cur.fetchall()

		# for details in r1:
		# 	bb.append(booking1(details))

		# sql3 = ("select hotel_name,check_in,check_out,fare,room_id from Room_Booking where customer_id=?")
		# cur.execute(sql3,(var.login_id,))
		# r1 = cur.fetchall()

		# for details in r1:
		# 	hb.append(booking2(details))

		
		form = rating()
		return render(request,'customers/mybookings.html',{'form':form,'bb':bb,'login':var.login})

	else:
		messages.error(request,"Log In to see your bookings")
		return redirect('customer_home')


def hbookings(request):
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):

		
		hb = []
		bb = []
		fb = []

		sql = ("select julianday('now') - julianday(?)")
		cur.execute(sql,('2020-05-11',))
		print(cur.fetchall()[0][0])

		sql3 = ("select hotel_name,check_in,check_out,fare,booking_id from Room_Booking where customer_id=?")
		cur.execute(sql3,(var.login_id,))
		r1 = cur.fetchall()

		for details in r1:
			hb.append(booking2(details))

		# sql2 = ("select start_point,destination,fare,date_of_journey,bus_id from Bus_Booking where customer_id=?")
		# cur.execute(sql2,(var.login_id,))
		# r1 = cur.fetchall()

		# for details in r1:
		# 	bb.append(booking1(details))

		# sql3 = ("select hotel_name,check_in,check_out,fare,room_id from Room_Booking where customer_id=?")
		# cur.execute(sql3,(var.login_id,))
		# r1 = cur.fetchall()

		# for details in r1:
		# 	hb.append(booking2(details))

		
		form = rating()
		return render(request,'customers/mybookings.html',{'form':form,'hb':hb,'login':var.login})

	else:
		messages.error(request,"Log In to see your bookings")
		return redirect('customer_home')


# def rf(request,id):
# 	import sqlite3
# 	connection = sqlite3.connect("database.db")
# 	cur = connection.cursor()

# 	rating = request.POST.get('rate')
# 	sql = ("update Flight_Booking set rating = ? where flight_id=? and customer_id=?")
# 	cur.execute(sql,(rating,id,var.login_id,))
# 	connection.commit()

# 	return redirect('mybookings')

def flight_booking(request,id):
	global dates
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	form = bookflight()
	
	if(var.login):
		if(request.method == 'POST'):

			form = bookflight(request.POST)
			dicti = request.POST.dict()
			print(dicti)
			
			no_of_seats = request.POST.get('no_of_seats')
			print(no_of_seats)
			# date_of_journey = request.POST.get('date_of_journey_year')+"-"+request.POST.get('date_of_journey_month')+"-"+request.POST.get("date_of_journey_day")
			date_of_journey = dates[-1]
			customer_id = var.login_id
			print(var.login_id)
			sql = ("select flight_id, start_point,destination,fare from Flight_Information where flight_id=?")
			cur.execute(sql,(id,))
			result = cur.fetchall()

			print(result)

			flight_id = result[0][0]
			start_point = result[0][1]
			destination = result[0][2]
			fare = result[0][3]

			to_db = [(flight_id,start_point,destination,customer_id,fare,date_of_journey,no_of_seats,)]

			connection.executemany("insert into Flight_Booking(flight_id,start_point,destination,customer_id,fare,date_of_journey,no_of_seats) values(?,?,?,?,?,?,?);",to_db)
			connection.commit()

			messages.success(request,"Booking Successsful")

			sql_ = ("select customer_email from Customer where customer_id=?")
			cur.execute(sql_,(customer_id,))
			result = cur.fetchall()
			print(result[0][0])

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls() 
			s.login("dbmstrial@gmail.com", "Dbmstrial@123") 
			message = "Your flight  with Flight Id "+flight_id+" from "+start_point+" to "+destination+" on "+date_of_journey+" has been booked successsfully"
			s.sendmail("dbmstrial@gmail.com", result[0][0], message) 
			s.quit() 

			return redirect('customer_home')
			# else:
			# 	return redirect('login')
		else:
			# rem_seats = Flightseats.objects.filter(flight=flight).first().remaining_seats
			# print(rem_seats)
			sql = ("select sum(no_of_seats) from Flight_Booking where flight_id=? and date_of_journey=?")
			cur.execute(sql,(id,dates[-1],))
			res = cur.fetchall()
			print(res)
			sql = ("select capacity from Flight_Information where flight_id=?")
			cur.execute(sql,(id,))
			capacity = cur.fetchall()

			print(res[0][0])
			if(res[0][0] is not  None):
				form.fields['no_of_seats'] = forms.IntegerField(max_value=capacity[0][0]-res[0][0])
			else:
				form.fields['no_of_seats'] = forms.IntegerField(max_value=capacity[0][0])
			# form.fields['date_of_journey'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			# 	empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'))
			# # date_of_journey = forms.DateField(widget=DatePickerInput)
			return render(request,'customers/flightbooking.html',{'form':form,'login':var.login})
	else:
		return redirect('login')


def bus_booking(request,id):
	global dates
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	form = bookbus()
	
	if(var.login):
		if(request.method == 'POST'):

			form = bookbus(request.POST)
			dicti = request.POST.dict()
			print(dicti)
			
			no_of_seats = request.POST.get('no_of_seats')
			print(no_of_seats)
			date_of_journey = dates[-1]
			customer_id = var.login_id
			print(var.login_id)
			sql = ("select bus_id, start_point,destination,fare from Bus_Information where bus_id=?")
			cur.execute(sql,(id,))
			result = cur.fetchall()

			print(result)

			bus_id = result[0][0]
			start_point = result[0][1]
			destination = result[0][2]
			fare = result[0][3]

			to_db = [(bus_id,start_point,destination,customer_id,fare,date_of_journey,no_of_seats,)]

			connection.executemany("insert into Bus_Booking(bus_id,start_point,destination,customer_id,fare,date_of_journey,no_of_seats) values(?,?,?,?,?,?,?);",to_db)
			connection.commit()

			messages.success(request,"Booking Successsful")

			sql_ = ("select customer_email from Customer where customer_id=?")
			cur.execute(sql_,(customer_id,))
			result = cur.fetchall()
			print(result[0][0])

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls() 
			s.login("dbmstrial@gmail.com", "Dbmstrial@123") 
			message = "Your bus with  Bus id "+bus_id+" from "+start_point+" to "+destination+" on "+date_of_journey+" has been booked successsfully"
			s.sendmail("dbmstrial@gmail.com", result[0][0], message) 
			s.quit() 


			return redirect('customer_home')
			# else:
			# 	return redirect('login')
		else:
			# rem_seats = Flightseats.objects.filter(flight=flight).first().remaining_seats
			# print(rem_seats)

			sql = ("select sum(no_of_seats) from Bus_Booking where bus_id=? and date_of_journey=?")
			cur.execute(sql,(id,dates[-1],))
			res = cur.fetchall()
			print(res)
			sql = ("select capacity from Bus_Information where bus_id=?")
			cur.execute(sql,(id,))
			capacity = cur.fetchall()

			print(res[0][0])
			if(res[0][0] is not  None):
				form.fields['no_of_seats'] = forms.IntegerField(max_value=capacity[0][0]-res[0][0])
			else:
				form.fields['no_of_seats'] = forms.IntegerField(max_value=capacity[0][0])
			# form.fields['date_of_journey'].widget=forms.SelectDateWidget(attrs={'class':'form-group'},
			# 	empty_label=("Choose Year", "Choose Month", "Choose Day"),years = ('2020','2021'))
			# # date_of_journey = forms.DateField(widget=DatePickerInput)
			return render(request,'customers/flightbooking.html',{'form':form,'login':var.login})

	else:
		return redirect('login')


def hotel_booking(request,id):
	global ind,oud
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	form = bookroom()
	
	if(var.login):
		if(request.method == 'POST'):

			form = bookroom(request.POST)
			dicti = request.POST.dict()
			print(dicti)
			
			

			# print("Res")
			# print(r)
			no_of_guests = request.POST.get('no_of_guests')
			# print(no_of_seats)
			check_in = ind[-1]
			check_out = oud[-1]
			customer_id = var.login_id
			print(var.login_id)
			sql = ("select fare, room_type,company_id,hotel_name from Room_Information where room_id=?")
			cur.execute(sql,(id,))
			result = cur.fetchall()

			print(result)

			


			fare = result[0][0]
			room_type = result[0][1]
			company_id = result[0][2]
			hotel_name = result[0][3]
			room_id = id

			sql = ("select hotel_address from Hotel where hotel_name=? and company_id=?")
			cur.execute(sql,(hotel_name,company_id,))
			res = cur.fetchall()

			address = res[0][0]

			to_db = [(company_id,hotel_name,address,customer_id,fare,room_type,check_in,check_out,no_of_guests,room_id,)]

			connection.executemany("insert into Room_Booking(company_id,hotel_name,address,customer_id,fare,room_type,check_in,check_out,no_of_guest,room_id) values(?,?,?,?,?,?,?,?,?,?);",to_db)
			connection.commit()

			messages.success(request,"Booking Successsful")

			to_db = [(id,no_of_guests,check_in,check_out,)]
			connection.executemany("insert into Rooms_left(room_id,no_of_guest,check_in,check_out) values(?,?,?,?);",to_db)
			connection.commit()

			sql_ = ("select customer_email from Customer where customer_id=?")
			cur.execute(sql_,(customer_id,))
			result = cur.fetchall()
			print(result[0][0])

			s = smtplib.SMTP('smtp.gmail.com', 587)
			s.starttls() 
			s.login("dbmstrial@gmail.com", "Dbmstrial@123") 
			message = "Your room has been booked successsfully"
			s.sendmail("dbmstrial@gmail.com", result[0][0] , message) 
			s.quit()

			return redirect('customer_home')
			# else:
			# 	return redirect('login')
		else:
			# rem_seats = Flightseats.objects.filter(flight=flight).first().remaining_seats
			# print(rem_seats)
			sql = ("select capacity from Room_Information where room_id=?")
			cur.execute(sql,(id,))
			res = cur.fetchall()

			form.fields['no_of_guests'] = forms.IntegerField(max_value=res[0][0])
			
			# date_of_journey = forms.DateField(widget=DatePickerInput)
			return render(request,'customers/hotelbooking.html',{'form':form,'login':var.login})

	else:
		return redirect('login')



def listflights(request,start_point,destination,fare,time):
	global dates
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	sql = ("select flight_id,airline_name,fare,capacity,departure_time,arrival_time,no_of_haults from Flight_Information natural join Airline where start_point = ? and destination=? and fare<=? and abs(strftime('%H', arrival_time) - strftime('%H', departure_time))<=? order by capacity DESC")
	cur.execute(sql,(start_point,destination,fare,time,))
	result = cur.fetchall()
	final_result = []
	for details in result:
		sql = ("select sum(no_of_seats) from Flight_Booking where flight_id=? and date_of_journey=?")
		cur.execute(sql,(details[0],dates[-1],))
		res = cur.fetchall()
		print(res)
		if(res[0][0] is None):
			final_result.append(flight(details))
		elif(details[3]>res[0][0]):
			details = list(details)
			details[3] = details[3] - res[0][0]
			final_result.append(flight(details))
	# for flight in result:
	# 	print(flight)
	# 	print(flight[7])

	return render(request,'customers/flightview.html',{'result':final_result,'login':var.login,'start_point':start_point,'destination':destination})


def listbuses(request,start_point,destination,fare,time):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
	print("I am here")

	sql = ("select bus_id,bus_name,fare,capacity,departure_time,arrival_time,no_of_haults from Bus_Information natural join Bus where start_point = ? and destination=? and fare<=? and abs(strftime('%H', arrival_time) - strftime('%H', departure_time))<=? order by capacity DESC")
	cur.execute(sql,(start_point,destination,fare,time,))

	result = cur.fetchall()
	final_result = []
	for details in result:
		sql = ("select sum(no_of_seats) from Bus_Booking where bus_id=? and date_of_journey=?")
		cur.execute(sql,(details[0],dates[-1],))
		res = cur.fetchall()
		print(res)
		if(res[0][0] is None):
			final_result.append(flight(details))
		elif(details[3]>res[0][0]):
			details = list(details)
			details[3] = details[3] - res[0][0]
			final_result.append(flight(details))
	# for flight in result:
	# 	print(flight)
	# 	print(flight[7])

	return render(request,'customers/busview.html',{'result':final_result,'login':var.login,'start_point':start_point,'destination':destination})


def listhotels(request,city,fare,room_type,parking):
	global ind,oud
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
	room_type = room_type + " - " + "Star Room"
	# room_type = "3 - Star Room"
	print(room_type)

	if(room_type=="None - Star Room"):
		sql = ("select h.hotel_name,h.city,h.hotel_address,h.parking_available,room_type,fare,capacity,wifi,breakfast,hot_water,ac,tv,heater,room_id from Room_Information r join Hotel h where r.hotel_name=h.hotel_name and r.company_id=h.company_id and h.city=? and r.fare<=?")
		cur.execute(sql,(city,fare,))
	else:
		sql = ("select h.hotel_name,h.city,h.hotel_address,h.parking_available,room_type,fare,capacity,wifi,breakfast,hot_water,ac,tv,heater,room_id from Room_Information r join Hotel h where r.hotel_name=h.hotel_name and r.company_id=h.company_id and h.city=? and r.room_type=? and r.fare<=?")
		cur.execute(sql,(city,room_type,fare,))

	result = cur.fetchall()
	print(result)
	check_in = int(ind[-1].split("-")[-1])
	check_out = int(oud[-1].split("-")[-1])
	tr = []
	
	for j in result:
		print(j[13])
		sql = ("select check_in,check_out from Rooms_left where room_id=?")
		cur.execute(sql,(j[13],))
		r = cur.fetchall()

		for i in range(len(r)):
			r1 = int(r[i][0].split("-")[-1])
			r2 = int(r[i][1].split("-")[-1])
			if((check_in>=r1 and check_in<r2) or (check_out>r1 and check_out<=r2) or (check_in<=r1 and check_out>=r2)):
				tr.append(j)
				print("removed")
				break
				# print("removed")

	for j in tr:
		result.remove(j)

	final_result = []
	for details in result:
		final_result.append(hotel(details))

	return render(request,'customers/hotelview.html',{'result':final_result,'login':var.login})
	# print(result)
