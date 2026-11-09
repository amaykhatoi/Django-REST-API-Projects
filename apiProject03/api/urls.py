from django.urls import path,include
# from .views import StudentAPI


# urlpatterns = [
#     path('students/',StudentAPI.as_view()),
#     path('students/<int:pk>/',StudentAPI.as_view())
# ]
# from .views import StudentListCreateAPI,StudentRetrieveUpdateDeleteAPI
# urlpatterns = [
#     path('student/',StudentListCreateAPI.as_view()),
#     path('student/<int:pk>/',StudentRetrieveUpdateDeleteAPI.as_view())
# ]

from rest_framework.routers import DefaultRouter
from .views import StudentviewSet

router = DefaultRouter()
router.register('students', StudentviewSet, basename='student')

urlpatterns = [
    path('',include(router.urls))
]

