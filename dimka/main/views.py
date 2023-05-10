from django.shortcuts import render, redirect



def index(request):
    return render(request,'main/index.html')


def about(request):
    return render(request,'main/about.html')


def python(request):
    return render(request,'main/python.html')


def picture(request):
    return render(request,'main/picture.html')




