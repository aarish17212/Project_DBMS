from django.urls import path

from . import views

urlpatterns = [
	path('',views.welcome_page_bus,name="bus_home"),
	path('add/',views.add_bus,name="add_new_bus"),
	path('update/<str:id>/',views.updateBus,name="update_bus"),
	path('delete/<str:id>/',views.deleteBus,name="delete_bus"),
	path('buses/announcement/',views.announcement,name="bus_announce"),
    # path('',views.home,name="customer_home"),
    # path('flights/',views.flights,name="customer_flights"),
   
]