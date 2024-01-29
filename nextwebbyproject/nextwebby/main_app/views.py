from django.shortcuts import render

def nextwebby(request):
    return render(request, 'index.html')

def pythondev(request):
    return render(request, 'role1.html')

def frontend(request):
    return render(request, 'role2.html')

def dataanalyst(request):
    return render(request, 'role3.html')