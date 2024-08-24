from django.shortcuts import render

def fun1(request, id):
    d={"students":[
        {"id": 2143281, "Name": "B.Purushotham", "total_sub": 6, "pass_sub": 6, "Fail_sub": 0},
        {"id": 2143297, "Name": "Sarfaraz", "total_sub": 6, "pass_sub": 6, "Fail_sub": 0},
        {"id": 21432114, "Name": "Sumanth", "total_sub": 6, "pass_sub": 6, "Fail_sub": 0},
        {"id": 21432133, "Name": "Tharun", "total_sub": 6, "pass_sub": 6, "Fail_sub": 2},
    ]}
    
    result = None
    for student in d["students"]:
        if student["id"] == id:
            result = student
            break
    
    context = {"result": result}
    return render(request, "student.html", context)
def fun2(request):
    return render(request,"boot.html")
