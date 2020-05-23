from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="customer_home"),
    # path('flights/',views.flights,name="customer_flights"),
    path('searchflight/',views.search_flight,name="searchflight"),
    path('searchbus/',views.search_bus,name="searchbus"),
    path('searchhotel/',views.search_hotel,name="searchhotel"),
    path('flights/booking/<str:id>/',views.flight_booking,name="flight_booking"),
    path('flights/<str:start_point>/<str:destination>/<int:fare>/<int:time>/',views.listflights,name="customer_flights"),
    path('buses/booking/<str:id>/',views.bus_booking,name="bus_booking"),
    path('buses/<str:start_point>/<str:destination>/<int:fare>/<int:time>/',views.listbuses,name="customer_buses"),
    path('hotels/<str:city>/<int:fare>/<str:room_type>/<str:parking>/',views.listhotels,name="customer_hotels"),
    path('hotels/booking/<str:id>/',views.hotel_booking,name="hotel_booking"),
    path('flightbookings/',views.fbookings,name="fbookings"),
    path('busbookings/',views.bbookings,name="bbookings"),
    path('hotelbookings/',views.hbookings,name="hbookings"),
    path('rateflight/<str:id>',views.rf,name="rate_flight"),
    path('ratebus/<str:id>',views.rb,name="rate_bus"),
    path('rateroom/<str:id>',views.rh,name="rate_hotel"),

]