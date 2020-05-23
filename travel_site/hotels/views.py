from django.shortcuts import render, redirect
from .forms import welcome_hotel_user_form, add_room_form, update_room_form, delete_room_form,announce
from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import var
from django.contrib import messages
from django.views.generic.edit import FormView, FormMixin
import announcements

# Create your views here.

class hotel:

	def __init__(self,details):
		self.room_type = details[0]
		self.capacity = details[1]
		self.fare = details[2]
		# self.hotel_name = details[3]
		self.room_id = details[9]
		# self.company_id = details[5]
		self.wifi = details[3]
		self.hot_water = details[4]
		self.ac = details[5]
		self.tv = details[6]
		self.heater = details[7]
		self.breakfast = details[8]
		


def welcome_page_hotel(request):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	form = welcome_hotel_user_form()
	print("Yes")
	if(request.method == 'POST'):
		get_choice = request.POST.get('action')

		if(get_choice=="Add New Room"):
			return redirect('add_new_room')

		elif(get_choice=="Add Announcement"):
			return redirect('hotel_announce')

	else:

		sql = ("select room_type,capacity,fare,wifi,hot_water,ac,tv,heater,breakfast,room_id from Room_Information where company_id=? order by room_id")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		final_result = []
		print(result)

		for details in result:
			final_result.append(hotel(details))

		sql = ("select count(city) as c , city from Room_Booking r join Hotel h where r.hotel_name = h.hotel_name and r.company_id=h.company_id group by city order by c DESC")
		cur.execute(sql)
		result = cur.fetchall()
		print(result)
		des = [None,None,None]
		for i in range(min(3,len(result))):
			des[i] = result[i][1]

		sql = ("select count(customer_id) as c, customer_id from Room_Booking where company_id=? group by customer_id order by c DESC")
		# sql = ("select * from Flight_Booking join Flight_Information where company_id=? and Flight_Information.flight_id = Flight_Booking.flight_id")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		print(result)
		cus = [None,None,None]
		for i in range(min(3,len(result))):
			cus[i] = result[i][1]


		sql = ("select count(room_type) as c , room_type from Room_Booking where company_id=? group by room_type order by c DESC")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()

		rt = [None,None,None]
		for i in range(min(3,len(result))):
			rt[i] = result[i][1]

		return render(request,'hotels/homePage.html',{'form':form,'login':var.login,'result':final_result,'des1':des[0],'des2':des[1],'des3':des[2],'cus1':cus[0],'cus2':cus[1],'cus3':cus[2],'r1':rt[0],'r2':rt[1],'r3':rt[2]})


def announcement(request):
	if(request.method=="POST"):
		announcement = request.POST.get('announcement')
		announcements.a.add(announcement)
		return redirect('hotel_home')
	else:
		form = announce()
		return render(request,'hotels/announcement.html',{'form':form,'login':var.login})
#------matching if company id exsist to airline
def add_room(request):
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):
		if(request.method== 'POST'):
			form = add_room_form(request.POST,request.FILES)
			if(form.is_valid()):
				print(var.login_id)
				company_id = var.login_id
				capacity = form.cleaned_data.get('capacity')
				room_type = form.cleaned_data.get('room_type')
				fare = form.cleaned_data.get('fare')
				wifi = form.cleaned_data.get('wifi')
				breakfast = form.cleaned_data.get('breakfast')
				ac = form.cleaned_data.get('ac')
				tv = form.cleaned_data.get('tv')
				hot_water = form.cleaned_data.get('hot_water')
				heater = form.cleaned_data.get('heater')

				# sql = ("select count(*) from Flight_Information where flight_id=?")
				# cur.execute(sql,(flight_id,))
				# result = cur.fetchall()

				# if(result[0][0]==0):
				sql = ("select hotel_name from Hotel where company_id=?")
				cur.execute(sql,(var.login_id,))
				hotel_name = cur.fetchall()[0][0]

				to_db = [(hotel_name,company_id,room_type,fare,capacity,wifi,breakfast,ac,tv,hot_water,heater)]
				connection.executemany("insert into Room_Information(hotel_name,company_id,room_type,fare,capacity,wifi,breakfast,ac,tv,hot_water,heater) values(?,?,?,?,?,?,?,?,?,?,?);",to_db)
				connection.commit()
				messages.success(request,"Congrats!, Room Added")
				return redirect('hotel_home')
				# else:
				# 	messages.error(request,"Flight Id already exists")
				# 	return redirect('add_new_flight')
				#--ADD a message showing data added
				
		else:
			form = add_room_form()
			return render(request,'hotels/addRoom.html',{'form':form,'login':var.login})

	else:
		return redirect('login')

def updateRoom(request,id):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	sql = ("select room_type,capacity,fare,wifi,hot_water,ac,tv,heater,breakfast from Room_Information where room_id=?")
	cur.execute(sql,(id,))
	result = cur.fetchall()

	if(var.login):
		if(request.method== 'POST'):
			form = update_room_form(request.POST,request.FILES)
			if(form.is_valid()):
				company_id = var.login_id
				company_id = var.login_id
				capacity = form.cleaned_data.get('capacity')
				room_type = form.cleaned_data.get('room_type')
				fare = form.cleaned_data.get('fare')
				wifi = form.cleaned_data.get('wifi')
				breakfast = form.cleaned_data.get('breakfast')
				ac = form.cleaned_data.get('ac')
				tv = form.cleaned_data.get('tv')
				hot_water = form.cleaned_data.get('hot_water')
				heater = form.cleaned_data.get('heater')

				# sql = ("select count(*) from Flight_Information where flight_id=?")
				# cur.execute(sql,(flight_id,))
				# result1 = cur.fetchall()

				# if(result1[0][0]==0):
				to_db = (room_type,fare,capacity,wifi,breakfast,ac,tv,hot_water,heater,id,)
				sql = ("update Room_Information set(room_type,fare,capacity,wifi,breakfast,ac,tv,hot_water,heater)=(?,?,?,?,?,?,?,?,?) where room_id=?")
				# connection.executemany("update Flight_information(flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) set(?,?,?,?,?,?,?,?,?) where flight_id=?",to_db)
				cur.execute(sql,to_db)
				connection.commit()

				messages.success(request,"Congrats!, Room Updated")
				return redirect('hotel_home')

				# elif(result[0][0]==flight_id):
				# 	to_db = (flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time,result[0][0],)
				# 	sql = ("update Flight_Information set(flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time)=(?,?,?,?,?,?,?,?,?) where flight_id=?")
				# 	# connection.executemany("update Flight_information(flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) set(?,?,?,?,?,?,?,?,?) where flight_id=?",to_db)
				# 	cur.execute(sql,to_db)
				# 	connection.commit()
				# 	messages.success(request,"Congrats!, Flight Updated")
				# 	return redirect('airline_home')

				# # else:
				# 	messages.error(request,"Flight Id already exists")
				# 	return redirect('update_flight',id)


				#--ADD a message showing data added
				
		else:

			

			initial = {'room_type':result[0][0],'capacity':result[0][1],'fare':result[0][2],'wifi':result[0][3],'hot_water':result[0][4],
			'ac':result[0][5],'tv':result[0][6],'heater':result[0][7],'breakfast':result[0][8]}

			form = update_room_form(initial=initial)
			return render(request,'hotels/updateRoom.html',{'form':form,'login':var.login})

	else:
		return redirect('login')


def deleteRoom(request,id):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):
		if(request.method== 'POST'):
			form = delete_room_form(request.POST,request.FILES)
			if(form.is_valid()):
				
				Yes = form.cleaned_data.get('Yes')
				if(Yes):
					sql = ("delete from Room_Information where room_id=?")
					cur.execute(sql,(id,))
					connection.commit()
					messages.success(request,"The Room has been deleted")
					return redirect('hotel_home')

				else:
					return redirect('hotel_home')
				#--ADD a message showing data added
				
		else:
			form = delete_room_form()
			return render(request,'hotels/deleteRoom.html',{'form':form,'login':var.login})

	else:
		redirect('login')


