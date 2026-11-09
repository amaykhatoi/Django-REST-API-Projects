from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.get_students, name='get_students'),
    path('students/add/',views.add_students, name='add_students'),
    path('students/update/<int:pk>/',views.update_students, name='update_students'),
    path('students/delete/<int:pk>/',views.delete_student, name='update_students'),
]
