from django.urls import path
from app import views
urlpatterns = [
    #static
    # path("january", views.Jan),
    # path("febuary",views.Feb),

    #dynamic path segment pattern 
    #order matter when comes to ocnversion
    #dynamic path with data type conversion
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge,name="monthly-challenge"),

    
    
]