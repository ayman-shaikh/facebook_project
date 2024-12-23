from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from . models import *

# Create your views here.

def home(request):
    #return HttpResponse("This is my first Django Project's Homepage.")
    return render(request, "home.html")

def account(request):
    return render(request, "account.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, **{"username":username, "password":password})
        print(user)
        if not user:
            print("User not found, please register")
        else:
            print("User found, logged in")
            auth_login(request, user)
            #print(request.user)
            return redirect("create_invoice")
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email_id = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=email_id, email=email_id, first_name=first_name, last_name=last_name, password=password)
        return redirect("login")
    return render(request, "register.html")

def create_invoice(request):
    if request.method == "POST":
        invoice_no = request.POST.get("invoiceNo")
        print(invoice_no)
        invoice_date = request.POST.get("invoiceDate")
        name = request.POST.get("name")
        address = request.POST.get("address")
        #total = request.POST.get("total")

        counter = request.POST.get("count")

        for i in range(int(counter)):
            product_description = request.POST.get("description"+str(i+1))
            quantity = request.POST.get("qty"+str(i+1))
            rate = request.POST.get("rate"+str(i+1))
            amount = request.POST.get("amount"+str(i+1))
            Invoice.objects.create(invoice_no=invoice_no, invoice_date=invoice_date, name=name, address=address, product_description=product_description, quantity=quantity, rate=rate, amount=amount, user=request.user)
        return redirect("view_invoice")
    return render(request, "create_invoice.html")

def view_invoice(request):
    invoices = Invoice.objects.all()
    context = {"invoice1": invoices}
    print(invoices.first())
    return render(request, "view_invoice.html", context)

def delete_invoice(request, pk):
    Invoice.objects.filter(id=pk).delete()
    invoices = Invoice.objects.all()
    context = {"invoice1": invoices}
    return render(request, "view_invoice.html", context)