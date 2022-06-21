from email import message
from django.shortcuts import redirect, render
from .models import contact as Contact
from django.contrib import messages
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contactdata=Contact(name=name,email=email,message=message)
        contactdata.save()
        messages.success(request,'We will stay in tuch!')
        return redirect('index')
        