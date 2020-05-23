from django import forms


choice = (("Add New Bus","Add New Bus"),("Make an Announcement","Make an Announcement"))


class welcome_bus_user_form(forms.Form):
	action = forms.ChoiceField(choices=choice,label='What are you looking for today ?',required=True,error_messages={'required': 'myRequiredMessage'})


class add_bus_form(forms.Form):

	bus_id = forms.CharField(label='Bus ID',required=True, max_length=50, error_messages={'required': 'myRequiredMessage'})
	start_point = forms.CharField(label='Start Point',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})
	destination = forms.CharField(label='Destination',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})
	capacity = forms.CharField(label='Capacity',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})
	no_of_haults = forms.CharField(label='Number Of Haults',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})
	fare = forms.CharField(label='Fare',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})
	arrival_time = forms.CharField(label='Arrival Time',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})
	departure_time = forms.CharField(label='Departure Time',required=True,max_length=100, error_messages={'required': 'myRequiredMessage'})

class update_bus_form(forms.Form):

	bus_id = forms.CharField(label='Bus ID',required=True, max_length=50, error_messages={'required': 'myRequiredMessage'})
	start_point = forms.CharField(label='Start Point')
	destination = forms.CharField(label='Destination')
	capacity = forms.CharField(label='Capacity')
	no_of_haults = forms.CharField(label='Number Of Haults')
	fare = forms.CharField(label='Fare')
	arrival_time = forms.CharField(label='Arrival Time')
	departure_time = forms.CharField(label='Departure Time')

class delete_bus_form(forms.Form):
	Yes = forms.BooleanField()

class announce(forms.Form):
	announcement = forms.CharField(max_length=200)


