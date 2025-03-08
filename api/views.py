# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from . serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# def studentsView(request):
#     student = Student.objects.all()
#     students_list = list(student.values())
#     return JsonResponse(students_list, safe=False)
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        # Get all the data from the students table
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def studentsDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

