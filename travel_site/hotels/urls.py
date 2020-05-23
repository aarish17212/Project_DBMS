from django.urls import path

from . import views

urlpatterns = [
	path('',views.welcome_page_hotel,name="hotel_home"),
	path('add/',views.add_room,name="add_new_room"),
	path('update/<str:id>/',views.updateRoom,name="update_room"),
	path('delete/<str:id>/',views.deleteRoom,name="delete_room"),
	path('hotels/announcement/',views.announcement,name="hotel_announce"),
    # path('',views.home,name="customer_home"),
    # path('flights/',views.flights,name="customer_flights"),
   
]