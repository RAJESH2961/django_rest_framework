# from django.shortcuts import render
# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from employees.models import Employee
from students.models import Student
from .serializers import EmployeeSerializer, StudentSerializer
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
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method =='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""      
#GENERICS
from rest_framework import generics, mixins

class EmployeeList(generics.ListCreateAPIView):# it is an combinaiotn of both List and create   
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # lookup_field = 'pk'
"""


#It will take lot of code viewsets.ViewSet but if we use Models.Viewset we can perform all in just 3 lines
from rest_framework import viewsets
class EmployeeViewset(viewsets.ModelViewSet):
    # def list(self, request):
    #     querySet = Employee.objects.all()
    #     serializer = EmployeeSerializer(querySet, many=True)
    #     return Response(serializer.data)
    
    # def create(self,request):
    #     serializer = EmployeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors)
    
    # def retrieve(self,request,pk=None):
    #     employee = get_object_or_404(Employee, pk=pk)
    #     serializer = EmployeeSerializer(employee)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def update(self, request, pk=None):
    #     employee = get_object_or_404(Employee, pk=pk)
    #     serializer = EmployeeSerializer(employee, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
    
    # def delete(self, request, pk=None):
    #     employee = get_object_or_404(Employee, pk=pk)
    #     employee.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
