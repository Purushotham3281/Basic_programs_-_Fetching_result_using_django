from django.shortcuts import render

# Create your views here.
def fun1(request,num1,num2):
    result=num1+num2
    d={"num1":num1,"num2":num2,"result":result}
    return render(request,"addition.html",d)
def fun2(request,num):
    result=num**2
    d={"num":num,"result":result}
    return render(request,"square.html",d)
def fun3(request, name1, name2):
    result = (sorted(name1) == sorted(name2))
    d = {"name1":name1,"name2":name2,"result": result}
    return render(request, "anagrams.html", d)
def fun4(request, num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    d = {"num":num,"result": result}
    return render(request, "factorial.html", d)
def fun5(request,num):
    result=0
    temp = num
    while temp > 0:
        digit = temp % 10
        result += digit ** 3
        temp //= 10
        arm=(result==num)
    d={"num":num,"result":arm}
    return render(request,"armstrong.html",d)
    
