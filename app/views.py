from django.shortcuts import render

# Create your views here.
def test1(request):
    return render(request,'test1.html')
def test2(request):
    return render(request,'test2.html')

def reg(request):
    return render(request,'reg.html')
def login(request):
    return render(request,'login.html')