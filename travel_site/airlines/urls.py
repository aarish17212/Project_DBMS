from django.urls import path

from . import views

urlpatterns = [
	path('',views.welcome_page_airline,name="airline_home"),
	path('add/',views.add_flight,name="add_new_flight"),
	path('update/<str:id>/',views.updateFlight,name="update_flight"),
	path('delete/<str:id>/',views.deleteFlight,name="delete_flight"),
	path('airline/announcement/',views.announcement,name="flight_announce"),
	# path('announcement/',views.announcement,name="flight_announce"),
    # path('',views.home,name="customer_home"),
    # path('flights/',views.flights,name="customer_flights"),
   
]