from rest_framework import serializers
from employees.models import Employee
from students.models import Student  # If Student model exists

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):  # Ensure correct name
    class Meta:
        model = Student
        fields = '__all__'
