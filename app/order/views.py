from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request,r"C:\Users\MEET SHAH\Desktop\React-JS-Complete-Course-master\Food Ordering App\app\order\templates\index.html")