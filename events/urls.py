from django.urls import path
from events import views

urlpatterns = [
    path('',views.event_description,name='events'),
    path('slotbooking/',views.slotbooking,name='slotbooking'),
    path('indoorimage/',views.indoorimages,name='indoorimage'),
    path('outdoorimage/',views.outdoorimages,name='outdoorimage'),
    # path('booking',views.booking_loc,name='booking')
    # path('door',views.event_doors,name='door')
    # path('booking_form', views.booking_view, name='booking'),
    path('success/', views.booking_success, name='booking_success'),
    path('booking/', views.booking_view, name='booking'),
    path('events/select-menu/', views.select_menu_view, name='select_menu'),
    path('confirmation/', views.confirmation_view, name='confirmation')
]
