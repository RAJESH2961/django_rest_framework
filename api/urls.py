from django.urls import include, path
from .import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employeedirectories')#for only viewset we have to use basename,Because it takes url based

urlpatterns = [
    path('students/',views.studentsView),
    # path('employees/', views.EmployeeList.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('', include(router.urls)),


    #blogs
    path('blogs/',views.BlogsView.as_view()),
    path('comments/',views.CommentsView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),



]
