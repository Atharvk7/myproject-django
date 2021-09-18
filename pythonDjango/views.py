from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def indexa(request):
    
    return render(request,"index.html")
#   return HttpResponse("this is home page")

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        product=request.POST.get("product")
        contact=Contact(name=name,email=email,password=password,address=address,product=product
    ,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')