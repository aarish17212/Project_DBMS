from django import forms



choices = (("Airline","Airline"),("Bus","Bus"),("Hotel","Hotel"),("Customer","Customer"))
gender_choices  = (("Male","Male"),("Female","Female"))

class UserRegistrationForm(forms.Form):

    email = forms.EmailField()
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=choices,
    label="Who Are You?", required=True, error_messages={'required': 'myRequiredMessage'})

class RegistrationCompletionForm(forms.Form):

    customer_gender = forms.ChoiceField(choices = gender_choices, label="Choose Gender",
     required=True, error_messages={'required': 'myRequiredMessage'})
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    customer_contact = forms.CharField(max_length=10)
    image = forms.ImageField(required=False)


class RegistrationCompletionForm_airline(forms.Form):

    airline_name = forms.CharField(max_length=20)
    company_id = forms.CharField(max_length=32)
    no_of_flights = forms.IntegerField(required=False)
    head_office = forms.CharField(max_length=20,required=False)
    # image = forms.ImageField(required=False)

class RegistrationCompletionForm_bus(forms.Form):

    bus_name = forms.CharField(max_length=20)
    company_id = forms.CharField(max_length=32)
    no_of_buses = forms.IntegerField(required=False)
    head_office = forms.CharField(max_length=20,required=False)

class RegistrationCompletionForm_hotel(forms.Form):

    hotel_name = forms.CharField(max_length=20)
    company_id = forms.CharField(max_length=32)
    no_of_rooms = forms.IntegerField(required=False)
    hotel_address = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    parking_available = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")))

class UserUpdateForm(forms.Form):
    email = forms.EmailField()


class ProfileUpdateForm(forms.Form):
	
    customer_gender = forms.ChoiceField(choices = gender_choices, label="Choose Gender",
     required=True, error_messages={'required': 'myRequiredMessage'})
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    customer_contact = forms.CharField(max_length=10)


class ProfileUpdateForm_airline(forms.Form):

    airline_name = forms.CharField(max_length=20)
    head_office = forms.CharField(max_length=20,required=False)

class ProfileUpdateForm_bus(forms.Form):

    bus_name = forms.CharField(max_length=20)
    head_office = forms.CharField(max_length=20,required=False)

class ProfileUpdateForm_hotel(forms.Form):

    hotel_name = forms.CharField(max_length=20)
    city = forms.CharField(max_length=20)
    parking_available = forms.ChoiceField(choices=(("Yes","Yes"),("No","No")))
    hotel_address = forms.CharField(max_length=20)

# class ProfileUpdateForm_hotel(forms.Form):

#     hotel_name = forms.Char


class loginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=choices,
    label="Who Are You?", required=True, error_messages={'required': 'myRequiredMessage'})
