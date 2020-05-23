from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, RegistrationCompletionForm, UserUpdateForm, ProfileUpdateForm, loginForm, ProfileUpdateForm_airline, ProfileUpdateForm_bus, RegistrationCompletionForm_airline, RegistrationCompletionForm_bus, RegistrationCompletionForm_hotel, ProfileUpdateForm_hotel
from django.contrib.auth.decorators import login_required
import var
from django import forms

store = []

def register(request):
	global store
	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	
	form = UserRegistrationForm()
	if (request.method == 'POST'):
		store = []
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		user_type = request.POST.get('user_type')

		# 
		sql = ("select count(*) from {} where {} =?".format(user_type,user_type.lower()+"_email"))
		cur.execute(sql,(email,))
		result = cur.fetchall()

		if(result[0][0]==0):
			if(password2==password1):
				store.append(email)
				store.append(password1)
				# user = User.objects.create_user(
		  #           email=email,user_type=user_type,password=password1
		  #       )
				# user.save()

				
				return redirect('./'+user_type.lower())

			else:
				messages.error(request,message="Password's don't match!")
				return render(request,'users/registration.html',{'form':form})

		else:
			messages.error(request,"Email Already exists!")
			return render(request,'users/registration.html',{'form':form})


	else:
		return render(request,'users/registration.html',{'form':form})

    # return render(request, 'register.html')


def update_profile(request,user):
	global store

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
		
	if(user=='customer'):
		if(request.method=="POST"):
			
			form = RegistrationCompletionForm(request.POST,request.FILES)
			if(form.is_valid()):
				first_name = form.cleaned_data.get('first_name')
				last_name = form.cleaned_data.get('last_name')
				customer_gender = form.cleaned_data.get('customer_gender')
				customer_contact = form.cleaned_data.get('customer_contact')
				customer_email = store[0]
				customer_password = store[1]
				print(customer_email)
				print(customer_password)
				to_db = [(first_name,last_name,customer_password,customer_email,customer_contact,customer_gender,'')]
				connection.executemany("insert into Customer(first_name,last_name,customer_password,customer_email,customer_contact,customer_gender,referal_code) values(?,?,?,?,?,?,?);",to_db)
				connection.commit()

				return redirect("login")

		else:
			form = RegistrationCompletionForm()

			return render(request,'users/RegistrationComplete.html',{'form':form,'email':store[0]})


	if(user=="airline"):
		if(request.method=="POST"):
			
			form = RegistrationCompletionForm_airline(request.POST,request.FILES)
			if(form.is_valid()):
				airline_name = form.cleaned_data.get('airline_name')
				company_id = form.cleaned_data.get('company_id')
				no_of_flights = form.cleaned_data.get('no_of_flights')
				head_office = form.cleaned_data.get('head_office')
				airline_email = store[0]
				airline_password = store[1]
				# print(customer_email)
				# print(customer_password)
				try:
					to_db = [(airline_name,company_id,airline_password,airline_email,no_of_flights,head_office)]
					connection.executemany("insert into Airline(airline_name,company_id,airline_password,airline_email,no_of_flights,head_office) values(?,?,?,?,?,?);",to_db)
					connection.commit()

				except:

					messages.error(request,"Company Id or airline_name already exists!")
					return redirect("update-profile",user)

				return redirect("login")

		else:
			form = RegistrationCompletionForm_airline()
			return render(request,'users/RegistrationComplete.html',{'form':form,'email':store[0]})


	if(user=="bus"):
		if(request.method=="POST"):
			
			form = RegistrationCompletionForm_bus(request.POST,request.FILES)
			if(form.is_valid()):
				bus_name = form.cleaned_data.get('bus_name')
				company_id = form.cleaned_data.get('company_id')
				no_of_buses = form.cleaned_data.get('no_of_buses')
				head_office = form.cleaned_data.get('head_office')
				bus_email = store[0]
				bus_password = store[1]
				# print(customer_email)
				# print(customer_password)

				try:
					to_db = [(bus_name,company_id,bus_password,bus_email,no_of_buses,head_office)]
					connection.executemany("insert into Bus(bus_name,company_id,bus_password,bus_email,no_of_buses,head_office) values(?,?,?,?,?,?);",to_db)
					connection.commit()

				except:
					messages.error(request,"Company Id or Bus Name already exists!")
					return redirect("update-profile",user)

				return redirect("login")

		else:
			form = RegistrationCompletionForm_bus()
			return render(request,'users/RegistrationComplete.html',{'form':form,'email':store[0]})

	if(user=="hotel"):
		if(request.method=="POST"):
			
			form = RegistrationCompletionForm_hotel(request.POST,request.FILES)
			if(form.is_valid()):
				hotel_name = form.cleaned_data.get('hotel_name')
				company_id = form.cleaned_data.get('company_id')
				no_of_rooms = form.cleaned_data.get('no_of_rooms')
				city = form.cleaned_data.get('city')
				hotel_address = form.cleaned_data.get('hotel_address')
				parking_available = form.cleaned_data.get('parking_available')
				hotel_email = store[0]
				hotel_password = store[1]
				# print(customer_email)
				# print(customer_password)

				try:
					to_db = [(hotel_name,company_id,city,hotel_password,hotel_email,hotel_address,no_of_rooms,parking_available)]
					connection.executemany("insert into Hotel(hotel_name,company_id,city,hotel_password,hotel_email,hotel_address,no_of_rooms,parking_available) values(?,?,?,?,?,?,?,?);",to_db)
					connection.commit()

				except:
					messages.error(request,"Company Id or Hotel name already exists!")
					return redirect("update-profile",user)

				return redirect("login")

		else:
			form = RegistrationCompletionForm_hotel()
			return render(request,'users/RegistrationComplete.html',{'form':form,'email':store[0]})



def login(request):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()
	

	form = loginForm()

	if(request.method=="POST"):

		form = loginForm(request.POST)
		user = request.POST.get('user_type')
		email = request.POST.get('email')
		password = request.POST.get('password')
		result = []

		if(user=="Customer"):
			
			print(email)
			print(type(email))
			sql = ("select customer_password,customer_id from Customer where customer_email=?")
			cur.execute(sql,(email,))
			result = cur.fetchall()

		elif(user=="Airline"):

			sql = ("select airline_password,company_id from Airline where airline_email=?")
			cur.execute(sql,(email,))
			result = cur.fetchall()

		elif(user=="Bus"):

			sql = ("select bus_password,company_id from Bus where bus_email=?")
			cur.execute(sql,(email,))
			result = cur.fetchall()

		elif(user=="Hotel"):

			sql = ("select hotel_password,company_id from Hotel where hotel_email=?")
			cur.execute(sql,(email,))
			result = cur.fetchall()

		if(len(result)==1):

			actual_pass = result[0][0]
			id = result[0][1]
			print(actual_pass)

			if(actual_pass==password):
				messages.success(request,"You are Logged In!")
				var.login = True
				var.login_type = user
				var.login_id = id
				print(var.login_id)
				print(str(user.lower())+"_"+"home")
				# return redirect('/airline/home/')
				return redirect(str(user.lower())+"_"+"home")
				# return redirect("customer_home")

			else:
				messages.error(request,"Password is Wrong. Remember, passwords are case sensitive.")
				return redirect('login')

		else:
			messages.error(request,"This Email doesn't exist.")
			return redirect('login')

		
	else:
		return render(request,'users/login.html',{'form':form})


def logout(request):
	var.login = False
	return render(request,'users/logout.html',{'login':var.login})


def profile(request):

	import sqlite3
	connection = sqlite3.connect("database.db")
	cur = connection.cursor()

	print(var.login)
	print(var.login_type)

	if(var.login==False):
		return redirect('login')
		
	else:

		u_form = UserUpdateForm()
		p_form = ProfileUpdateForm()

		if(var.login_type=="Customer"):
			
			p_form = ProfileUpdateForm()

			if request.method == 'POST':
				u_form = UserUpdateForm(request.POST)
				p_form = ProfileUpdateForm(request.POST,
		                                   request.FILES)

				
				if u_form.is_valid() and p_form.is_valid():

					try:
						sql = ('update Customer set customer_email = ? where customer_id = ?')
						cur.execute(sql,(u_form.cleaned_data.get('email'),var.login_id,))
						connection.commit()

					except:
						messages.error(request,"Email Already Exists!")
						return redirect('profile')

					sql1 = ('update Customer set customer_contact=  ? where customer_id = ?')
					sql2 = ('update Customer set customer_gender=  ? where customer_id = ?')
					sql3 = ('update Customer set first_name=  ? where customer_id = ?')
					sql4 = ('update Customer set last_name=  ? where customer_id = ?')

					cur.execute(sql1,(p_form.cleaned_data.get('customer_contact'),var.login_id,))
					cur.execute(sql2,(p_form.cleaned_data.get('customer_gender'),var.login_id,))
					cur.execute(sql3,(p_form.cleaned_data.get('first_name'),var.login_id,))
					cur.execute(sql4,(p_form.cleaned_data.get('last_name'),var.login_id,))

					connection.commit()

					messages.success(request, f'Your account has been updated!')
					return redirect('profile')

			else:
				
				sql = ("select * from Customer where customer_id=?")
				cur.execute(sql,(var.login_id,))
				result = cur.fetchall()

				
				initial = {'customer_contact':result[0][5],'customer_gender':result[0][6],'first_name':result[0][0],'last_name':result[0][1]}
				u_form =  UserUpdateForm(initial={'email':result[0][4]})
				p_form = ProfileUpdateForm(initial=initial)

				context = {

					'u_form': u_form,
					'p_form': p_form,
					'first_name': result[0][0],
					'last_name': result[0][1],
					'customer_email': result[0][4],
					'customer_contact': result[0][5],
					'customer_gender': result[0][6],
					'login':var.login,

			    }

				return render(request, 'users/profile.html', context)

		elif(var.login_type=="Airline"):

			p_form = ProfileUpdateForm_airline()

			sql = ("select airline_email, airline_name, head_office from Airline where company_id=?")
			cur.execute(sql,(var.login_id,))
			result = cur.fetchall()

			if request.method == 'POST':
				u_form = UserUpdateForm(request.POST)
				p_form = ProfileUpdateForm_airline(request.POST,
		                                   request.FILES)

				
				if u_form.is_valid() and p_form.is_valid():

					if(u_form.cleaned_data.get('email')!=result[0][0]):

						try:
							sql = ('update Airline set airline_email = ? where company_id = ?')
							cur.execute(sql,(u_form.cleaned_data.get('email'),var.login_id,))
							connection.commit()

						except:
							messages.error(request,"Email Already Exists!")
							return redirect('profile')

					sql1 = ('update Airline set airline_name =  ? where company_id = ?')
					sql2 = ('update Airline set head_office =  ? where company_id = ?')

					if(p_form.cleaned_data.get('airline_name')!=result[0][1]):
						try:
							print("entered_")
							cur.execute(sql1,(p_form.cleaned_data.get('airline_name'),var.login_id,))
							connection.commit()

						except:
							messages.error(request,"Airline Name already exists!")
							return redirect('profile')
						
					cur.execute(sql2,(p_form.cleaned_data.get('head_office'),var.login_id,))
					connection.commit()

					messages.success(request, f'Your account has been updated!')
					return redirect('profile')

			else:
				
				initial = {'airline_name':result[0][1],'head_office':result[0][2]}
				u_form =  UserUpdateForm(initial={'email':result[0][0]})
				p_form = ProfileUpdateForm_airline(initial=initial)

				context = {

					'u_form': u_form,
					'p_form': p_form,
					'airline_name': result[0][1],
					'head_office': result[0][2],
					'airline_email': result[0][0],
					'login':var.login,

			    }

				return render(request, 'users/profile.html', context)

		elif(var.login_type=="Bus"):

			p_form = ProfileUpdateForm_bus()

			sql = ("select bus_email, bus_name, head_office from Bus where company_id=?")
			cur.execute(sql,(var.login_id,))
			result = cur.fetchall()

			if request.method == 'POST':
				u_form = UserUpdateForm(request.POST)
				p_form = ProfileUpdateForm_bus(request.POST,
		                                   request.FILES)

				
				if u_form.is_valid() and p_form.is_valid():

					if(u_form.cleaned_data.get('email')!=result[0][0]):
						try:
							sql = ('update Bus set bus_email = ? where company_id = ?')
							cur.execute(sql,(u_form.cleaned_data.get('email'),var.login_id,))
							connection.commit()

						except:
							messages.error(request,"Email Already Exists!")
							return redirect('profile')

					sql1 = ('update Bus set bus_name =  ? where company_id = ?')
					sql2 = ('update Bus set head_office =  ? where company_id = ?')

					if(p_form.cleaned_data.get('bus_name')!=result[0][1]):
						try:
							cur.execute(sql1,(p_form.cleaned_data.get('bus_name'),var.login_id,))
							connection.commit()

						except:
							messages.error(request,"Bus Name already exists!")
							return redirect('profile')
						
					cur.execute(sql2,(p_form.cleaned_data.get('head_office'),var.login_id,))
					connection.commit()

					messages.success(request, f'Your account has been updated!')
					return redirect('profile')

			else:

				initial = {'bus_name':result[0][1],'head_office':result[0][2]}
				u_form =  UserUpdateForm(initial={'email':result[0][0]})
				p_form = ProfileUpdateForm_bus(initial=initial)

				context = {

					'u_form': u_form,
					'p_form': p_form,
					'bus_name': result[0][1],
					'head_office': result[0][2],
					'bus_email': result[0][0],
					'login':var.login,

			    }

				return render(request, 'users/profile.html', context)


		elif(var.login_type=="Hotel"):

			p_form = ProfileUpdateForm_hotel()

			sql = ("select hotel_email, hotel_name,city,parking_available,hotel_address from Hotel where company_id=?")
			cur.execute(sql,(var.login_id,))
			result = cur.fetchall()

			if request.method == 'POST':
				u_form = UserUpdateForm(request.POST)
				p_form = ProfileUpdateForm_hotel(request.POST,
		                                   request.FILES)

				
				if u_form.is_valid() and p_form.is_valid():

					if(u_form.cleaned_data.get('email')!=result[0][0]):
						try:
							sql = ('update Hotel set hotel_email = ? where company_id = ?')
							cur.execute(sql,(u_form.cleaned_data.get('email'),var.login_id,))
							connection.commit()

						except:
							messages.error(request,"Email Already Exists!")
							return redirect('profile')

					hotel_name = p_form.cleaned_data.get('hotel_name')
					city = p_form.cleaned_data.get('city')
					parking_available = p_form.cleaned_data.get('parking_available')
					hotel_address = p_form.cleaned_data.get('hotel_address')

					to_db = (city,parking_available,hotel_address,var.login_id,)
					sql1 = ("update Hotel set(city,parking_available,hotel_address)=(?,?,?) where company_id=?")
					# connection.executemany("update Flight_information(flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) set(?,?,?,?,?,?,?,?,?) where flight_id=?",to_db)
					

					if(p_form.cleaned_data.get('hotel_name')!=result[0][1]):
						try:
							sql = ("update Hotel set(hotel_name)=(?) where company_id=?")
							cur.execute(sql,(hotel_name,))
							connection.commit()

						except:
							messages.error(request,"Hotel Name already exists!")
							return redirect('profile')
					
						

					cur.execute(sql1,to_db)
					connection.commit()

					messages.success(request, f'Your account has been updated!')
					return redirect('profile')


			else:

				initial = {'hotel_name':result[0][1],'city':result[0][2],'parking_available':result[0][3],'hotel_address':result[0][4]}
				u_form =  UserUpdateForm(initial={'email':result[0][0]})
				p_form = ProfileUpdateForm_hotel(initial=initial)

				context = {

					'u_form': u_form,
					'p_form': p_form,
					'login':var.login,

			    }

				return render(request, 'users/profile.html', context)



# def login_success(request):
# 	if(request.user.user_type=="Customer"):
# 		return redirect('./customer')
