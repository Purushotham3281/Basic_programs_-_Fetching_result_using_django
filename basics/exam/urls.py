
from django.urls import path
from exam import views

urlpatterns = [
    path('roll/<int:id>', views.fun1, name='student_details'),
    path("boot",views.fun2,name="boots")
]
