from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serialzers import StudentSerializer
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def student_list(request):
    Students =  Student.objects.all()
    serialzer = StudentSerializer(Students, many=True)
    return Response(serialzer.data)