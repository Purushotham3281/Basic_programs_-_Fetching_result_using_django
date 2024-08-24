from django.urls import path
from programs import views
urlpatterns=[
    path("add/<int:num1>/<int:num2>",views.fun1,name="addition_of_numbers"),
    path("square/<int:num>",views.fun2,name="square_of_a_number"),
    path("anagram/<str:name1>/<str:name2>",views.fun3,name="anagrams_detection"),
    path("factorial/<int:num>",views.fun4,name="factorial"),
    path("armstrong/<int:num>",views.fun5,name="armstrong_detection")

]