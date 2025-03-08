from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    return HttpResponse('<h2>Hello world!</h2>')

def students(request):
    student = [
        {
        'id' : 12,
        'name' : 'rajesh',
        'age' : 23
        }
    ]
    return HttpResponse(student)
