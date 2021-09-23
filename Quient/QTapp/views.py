from django.shortcuts import render,HttpResponseRedirect,redirect
from datetime import datetime
from QTapp.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
  return render(request,'Home.html')
def about(request):
  return render(request,'About.html') 
def Testimonials(request):
  return render(request,'Testimonials.html')   
def Gallery(request):
  return render(request,'Gallery.html')

#This fuction to Insert all contacts in database
def contact(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')


    #validation
    error_message = None
    if not name:
      error_message = "Name Required!"
    elif not email:
      error_message = "Email is Required!"
    elif len(email)<6:
      error_message = "Enter the correct Email"
    elif not phone:
      error_message = "Phone Number Required!"
    elif len(phone)<=10:
      error_message = "Phone Number must be 10 char long"
    elif not desc:
      error_message = "message is required"

    #validation is valid this will save
    if not  error_message:
      contact = Contact(name=name , email=email, phone=phone, desc=desc, date=datetime.today())
      contact.save()
      messages.success(request,'Thank you for contacting us')
      return redirect(home)
    else:
      messages.success(request,'There is error! Please try again')
      return render(request,'contact.html',{'error':error_message})
  return render(request,'contact.html')   


#This fuction to View all contacts in database
def Viewdb(request):

  contact_info = Contact.objects.all()
  return render(request,'Viewdb.html',{'info':contact_info})

#This fuction to delete in View all contacts in database
def delete_data(request,id):
  if request.method == 'POST':
    deleted = Contact.objects.get(pk=id)
    deleted.delete()
    messages.success(request,'Deleted Successfully')
    return redirect(Viewdb)

#This fuction is search contact in view(query = q)
def search_contacts(request):
  q = request.GET['q']
  notfound_message = None
  if 'q' in request.GET:
    infoname = Contact.objects.filter(name=q)
    infoemail =Contact.objects.filter(email=q)
    infophone = Contact.objects.filter(phone=q)
    info = infoname.union(infoemail).union(infophone)
  else:
    notfound_message= "Your searching contacts is not in list"
    info = Contact.objects.all()
    return render(request,'Viewdb.html',{'info':info,'notfound':notfound_message})
  return render(request,'Viewdb.html',{'info':info})