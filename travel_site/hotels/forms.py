from django import forms


choice = (("Add New Room","Add New Room"),("Add Announcement","Add Announcement"))
choice2 = (("1 - Star Room","1 - Star Room"),("2 - Star Room","2 - Star Room"),("3 - Star Room","3 - Star Room"),("4 - Star Room","4 - Star Room"),("5 - Star Room","5 - Star Room"),("6 - Star Room","6 - Star Room"))
choice3 = (("Yes","Yes"),("No","No"))

class welcome_hotel_user_form(forms.Form):
	action = forms.ChoiceField(choices=choice,label='What are you looking for today ?',required=True,error_messages={'required': 'myRequiredMessage'})


class add_room_form(forms.Form):

	room_type = forms.ChoiceField(choices=choice2,label='Room Type',required=True,error_messages={'required': 'myRequiredMessage'})
	capacity = forms.CharField(label='Capacity',required=True, max_length=50, error_messages={'required': 'myRequiredMessage'})
	fare = forms.CharField(label='Fare',required=True, max_length=50, error_messages={'required': 'myRequiredMessage'})
	# room_id = forms.CharField(label='Room ID',required=True, max_length=50, error_messages={'required': 'myRequiredMessage'})
	wifi = forms.ChoiceField(choices=choice3)
	hot_water = forms.ChoiceField(choices=choice3)
	ac = forms.ChoiceField(choices=choice3)
	heater = forms.ChoiceField(choices=choice3)
	tv = forms.ChoiceField(choices=choice3)
	breakfast = forms.ChoiceField(choices=choice3)
	

	
	
class update_room_form(forms.Form):


	room_type = forms.ChoiceField(choices=choice2,label='Room Type',required=True,error_messages={'required': 'myRequiredMessage'})
	capacity = forms.CharField(label='Capacity')
	fare = forms.CharField(label='Fare')
	# company_id = forms.CharField(label='Company ID')
	wifi = forms.ChoiceField(choices=choice3)
	hot_water = forms.ChoiceField(choices=choice3)
	ac = forms.ChoiceField(choices=choice3)
	heater = forms.ChoiceField(choices=choice3)
	tv = forms.ChoiceField(choices=choice3)
	breakfast = forms.ChoiceField(choices=choice3)

class delete_room_form(forms.Form):
	Yes = forms.BooleanField()


class announce(forms.Form):
	announcement = forms.CharField(max_length=200)