
from django.contrib import admin
from django.urls import path
from restapp1 import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/getallstudents', views.getallstudents, name="getallstudents"),
    path('api/getstudent/<int:id>', views.get_student, name='getstudent'),
    path('api/createstudent', views.create_student, name='createstudent'),
    path('api/deletestudent/<int:id>', views.delete_student, name='deletestudent'),
    path('api/updatestudent/<int:id>', views.update_student, name='updatestudent')
]
