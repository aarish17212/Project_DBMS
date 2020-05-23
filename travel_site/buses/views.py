from django.shortcuts import render, redirect
from .forms import welcome_bus_user_form, add_bus_form, update_bus_form, delete_bus_form, announce
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

class bus:

	def __init__(self,details):
		self.bus_id = details[0]
		self.fare = details[1]
		self.capacity = details[2]
		self.departure_time = details[3]
		self.arrival_time = details[4]
		self.no_of_haults = details[5]
		self.start_point = details[6]
		self.destination = details[7]

def welcome_page_bus(request):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	form = welcome_bus_user_form()
	print("Yes")
	if(request.method == 'POST'):
		get_choice = request.POST.get('action')

		if(get_choice=="Add New Bus"):
			return redirect('add_new_bus')

		elif(get_choice == "Make an Announcement"):
			return redirect('bus_announce')
	else:

		sql = ("select bus_id,fare,capacity,departure_time,arrival_time,no_of_haults,start_point,destination from Bus_Information where company_id=? order by bus_id")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		final_result = []

		for details in result:
			final_result.append(bus(details))

		sql = ("select count(destination) as c , destination from Bus_Booking group by destination order by c DESC")
		cur.execute(sql)
		result = cur.fetchall()
		print(result)
		des = [None,None,None]
		for i in range(min(3,len(result))):
			des[i] = result[i][1]

		sql = ("select count(customer_id) as c, customer_id from (select * from Bus_Booking join Bus_Information where company_id=? and Bus_Information.bus_id = Bus_Booking.bus_id) as r natural join Customer group by customer_id order by c DESC")
		# sql = ("select * from Bus_Booking join Bus_Information where company_id=? and Bus_Information.bus_id = Bus_Booking.bus_id")
		cur.execute(sql,(var.login_id,))
		result = cur.fetchall()
		print(result)
		cus = [None,None,None]
		for i in range(min(3,len(result))):
			cus[i] = result[i][1]

		return render(request,'buses/homePage.html',{'form':form,'login':var.login,'result':final_result,'des1':des[0],'des2':des[1],'des3':des[2],'cus1':cus[0],'cus2':cus[1],'cus3':cus[2]})

def announcement(request):
	if(request.method=="POST"):
		announcement = request.POST.get('announcement')
		announcements.a.add(announcement)
		return redirect('bus_home')
	else:
		form = announce()
		return render(request,'buses/announcement.html',{'form':form,'login':var.login})
#------matching if company id exsist to bus
def add_bus(request):
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):
		if(request.method== 'POST'):
			form = add_bus_form(request.POST,request.FILES)
			if(form.is_valid()):
				print(var.login_id)
				company_id = var.login_id
				bus_id = form.cleaned_data.get('bus_id')
				start_point = form.cleaned_data.get('start_point')
				destination = form.cleaned_data.get('destination')
				capacity = form.cleaned_data.get('capacity')
				no_of_haults = form.cleaned_data.get('no_of_haults')
				fare = form.cleaned_data.get('fare')
				arrival_time = form.cleaned_data.get('arrival_time')
				departure_time = form.cleaned_data.get('departure_time')

				sql = ("select count(*) from Bus_Information where bus_id=?")
				cur.execute(sql,(bus_id,))
				result = cur.fetchall()

				if(result[0][0]==0):
					to_db = [(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time)]
					connection.executemany("insert into Bus_Information(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) values(?,?,?,?,?,?,?,?,?);",to_db)
					connection.commit()
					messages.success(request,"Congrats!, bus Added")

					# for i in range(30):
					# 	to_db = [(bus_id,"2020-5-"+str(i),capacity,)]
					# 	connection.executemany("insert into Bus_seats(bus_id,booking_date,seats) values(?,?,?);",to_db)
					# 	connection.commit()

					return redirect('bus_home')
				else:
					messages.error(request,"bus Id already exists")
					return redirect('add_new_bus')
				#--ADD a message showing data added
				
		else:
			form = add_bus_form()
			return render(request,'buses/addbus.html',{'form':form,'login':var.login})

	else:
		return redirect('login')

def updateBus(request,id):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	sql = ("select bus_id,fare,capacity,departure_time,arrival_time,no_of_haults,start_point,destination from Bus_Information where bus_id=?")
	cur.execute(sql,(id,))
	result = cur.fetchall()

	if(var.login):
		if(request.method== 'POST'):
			form = update_bus_form(request.POST,request.FILES)
			if(form.is_valid()):
				company_id = var.login_id
				bus_id = form.cleaned_data.get('bus_id')
				start_point = form.cleaned_data.get('start_point')
				destination = form.cleaned_data.get('destination')
				capacity = form.cleaned_data.get('capacity')
				no_of_haults = form.cleaned_data.get('no_of_haults')
				fare = form.cleaned_data.get('fare')
				arrival_time = form.cleaned_data.get('arrival_time')
				departure_time = form.cleaned_data.get('departure_time')

				sql = ("select count(*) from Bus_Information where bus_id=?")
				cur.execute(sql,(bus_id,))
				result1 = cur.fetchall()

				if(result1[0][0]==0):
					to_db = (bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time,result[0][0],)
					sql = ("update Bus_Information set(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time)=(?,?,?,?,?,?,?,?,?) where bus_id=?")
					# connection.executemany("update Bus_Information(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) set(?,?,?,?,?,?,?,?,?) where bus_id=?",to_db)
					cur.execute(sql,to_db)
					connection.commit()

					messages.success(request,"Congrats!, bus Updated")
					return redirect('bus_home')

				elif(result[0][0]==bus_id):
					to_db = (bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time,result[0][0],)
					sql = ("update Bus_Information set(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time)=(?,?,?,?,?,?,?,?,?) where bus_id=?")
					# connection.executemany("update Bus_Information(bus_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) set(?,?,?,?,?,?,?,?,?) where bus_id=?",to_db)
					cur.execute(sql,to_db)
					connection.commit()
					messages.success(request,"Congrats!, bus Updated")
					return redirect('bus_home')

				else:
					messages.error(request,"bus Id already exists")
					return redirect('update_bus',id)


				#--ADD a message showing data added
				return redirect('bus_home')
		else:

			

			initial = {'bus_id':result[0][0],'fare':result[0][1],'capacity':result[0][2],'departure_time':result[0][3],'arrival_time':result[0][4],
			'no_of_haults':result[0][5],'start_point':result[0][6],'destination':result[0][7]}

			form = update_bus_form(initial=initial)
			return render(request,'buses/updatebus.html',{'form':form,'login':var.login})

	else:
		return redirect('login')


def deleteBus(request,id):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	if(var.login):
		if(request.method== 'POST'):
			form = delete_bus_form(request.POST,request.FILES)
			if(form.is_valid()):
				
				Yes = form.cleaned_data.get('Yes')
				if(Yes):
					sql = ("delete from Bus_Information where bus_id=?")
					cur.execute(sql,(id,))
					connection.commit()
					messages.success(request,"The bus has been deleted")
					return redirect('bus_home')

				else:
					return redirect('bus_home')
				#--ADD a message showing data added
				
		else:
			form = delete_bus_form()
			return render(request,'buses/deletebus.html',{'form':form,'login':var.login})

	else:
		redirect('login')


