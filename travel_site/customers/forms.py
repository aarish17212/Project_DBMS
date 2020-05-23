from django import forms

import sqlite3
connection = sqlite3.connect("database.db")
cur = connection.cursor()

sql = ("select start_point, destination from Flight_Information")
cur.execute(sql)
result = cur.fetchall()

starts = []
ends = []

for i in range(len(result)):
	if result[i][0] not in starts:
		starts.append(result[i][0])


for i in range(len(result)):
	if result[i][1] not in ends:
		ends.append(result[i][1])

f_starts = []
f_ends = []

for start in starts:
	f_starts.append((start,start))

for end in ends:
	f_ends.append((end,end))

f_starts = tuple(f_starts)
f_ends = tuple(f_ends)

sql = ("select start_point, destination from Bus_Information")
cur.execute(sql)
result = cur.fetchall()

starts = []
ends = []
fi_starts = []
fi_ends = []
for i in range(len(result)):
	if result[i][0] not in starts:
		starts.append(result[i][0])


for i in range(len(result)):
	if result[i][1] not in ends:
		ends.append(result[i][1])


for start in starts:
	fi_starts.append((start,start))

for end in ends:
	fi_ends.append((end,end))

fi_starts = tuple(fi_starts)
fi_ends = tuple(fi_ends)

cities = []
sql = ("select city from Hotel")
cur.execute(sql)
result = cur.fetchall()
for i in range(len(result)):
	if((result[i][0],result[i][0]) not in cities):
		cities.append((result[i][0],result[i][0]))

cities = tuple(cities)

choices = (("flights","flights"),("buses","buses"),("hotels","hotels"))

class search_form(forms.Form):
	search = forms.ChoiceField(choices = choices,
    label="Search", required=True, error_messages={'required': 'myRequiredMessage'})


class search_flights(forms.Form):

	date = forms.DateField()

	start_point = forms.ChoiceField(choices = f_starts,
    label="Select Source", required=True, error_messages={'required': 'myRequiredMessage'})

	destination = forms.ChoiceField(choices = f_ends,
    label="Select Destination", required=True, error_messages={'required': 'myRequiredMessage'})

	max_budget = forms.IntegerField(required=False)

	max_time_in_hrs = forms.IntegerField(required=False)


class bookflight(forms.Form):

	no_of_seats = forms.IntegerField(max_value=500)
	# date_of_journey = forms.DateField()


class search_buses(forms.Form):

	date = forms.DateField()

	start_point = forms.ChoiceField(choices = fi_starts,
    label="Select Source", required=True, error_messages={'required': 'myRequiredMessage'})

	destination = forms.ChoiceField(choices = fi_ends,
    label="Select Destination", required=True, error_messages={'required': 'myRequiredMessage'})

	max_budget = forms.IntegerField(required=False)

	max_time_in_hrs = forms.IntegerField(required=False)

class search_hotels(forms.Form):

	check_in = forms.DateField()
	check_out = forms.DateField()

	city = forms.ChoiceField(choices = cities,
    label="Select City", required=True, error_messages={'required': 'myRequiredMessage'})

	max_budget = forms.IntegerField(required=False)

	room = forms.ChoiceField(choices=(("None","None"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6")),required=False)

	parking = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")),required=False)

class bookbus(forms.Form):

	no_of_seats = forms.IntegerField(max_value=500)
	# date_of_journey = forms.DateField()

class bookroom(forms.Form):
	no_of_guests = forms.IntegerField()

class rating(forms.Form):
	Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
	)

	rate = forms.ChoiceField(choices=Rating_CHOICES,required=False)