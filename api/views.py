# from django.shortcuts import render
# from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from employees.models import Employee
from students.models import Student
from .serializers import EmployeeSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from employees.filters import EmployeeFilter

from rest_framework.filters import SearchFilter, OrderingFilter

#custom PAgination
# from . blogs import CustomPagination
from blogs.paginations import CustomPagination
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
    #Adding custom pagination
    pagination_class = CustomPagination
    # filterset_fields = ['designation']
    filterset_class = EmployeeFilter

from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from rest_framework import generics, mixins

class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title', 'blog_body']
    # search_fields = ['^blog_title'] # Exactly starts with 
    ordering_fields = ['id', 'blog_title']


class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'