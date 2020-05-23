# from django.db import models
# from users.models import Airline

# class FlightInformation(models.Model):
# 	company = models.OneToOneField(Airline,on_delete=models.CASCADE)
# 	flight_id = models.CharField(max_length=20,primary_key=True)
# 	start_point = models.CharField(max_length=20)
# 	destination = models.CharField(max_length=20)
# 	capacity = models.IntegerField()
# 	no_of_hautls = models.IntegerField(default=0)
# 	fare = models.IntegerField()
# 	arrival_time = models.TimeField()
# 	departure_time = models.TimeField()