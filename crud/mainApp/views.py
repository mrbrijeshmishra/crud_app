from django.shortcuts import render,redirect
from .models import Employee
from django.db.models import Q

def home(Request):
    if (Request.method == "POST"):
        search = Request.POST.get("search")
        data = Employee.objects.filter(Q(name__icontains=search)|Q(email__icontains=search))
    else:
        data = Employee.objects.all()
    return render(Request,"index.html",{'data':data})

def delete(Request,id):
    data = Employee.objects.get(id=id)
    if(data):
        data.delete()
    return redirect("/")

def addRecord(Request):
    if (Request.method=="POST"):
        e = Employee()
        e.name = Request.POST['fame']
        e.email = Request.POST['email']
        e.phone = Request.POST['phone']
        e.sal = Request.POST['salary']
        e.city = Request.POST['city']
        e.state = Request.POST['state']
        e.save()
        return redirect("/")
    return render(Request,'add.html')

# Another way to write post and get method
# def addRecord(Request):
#     if (Request.method=="POST"):
#         e = Employee()
#         e.name = Request.POST.get('fame')
#         e.email = Request.POST.get('email')
#         e.phone = Request.POST.get('phone')
#         e.sal = Request.POST.get('salary')
#         e.city = Request.POST.get('city')
#         e.state = Request.POST.get('state')
#         e.save()
#         return redirect("/")
#     return render(Request,'add.html')

# Here i have given fame in [] we did it because in html file in name input we have passed name of that as fame.
# e.name means e is object of employee class and name is the field name we have given in that table.
# e.save() is used to dave data in table.

def updateRecord(Request,id):
    ndata = Employee.objects.get(id=id)
    if (Request.method=="POST"):
        ndata.name = Request.POST.get('name')
        ndata.email = Request.POST.get('email')
        ndata.phone = Request.POST.get('phone')
        ndata.sal = Request.POST.get('salary')
        ndata.city = Request.POST.get('city')
        ndata.state = Request.POST.get('state')
        ndata.save()
        return redirect("/")
    return render(Request,"update.html",{'ndata':ndata})