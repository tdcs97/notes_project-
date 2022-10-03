import email
from multiprocessing import context
from pyexpat.errors import messages
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render

from demo_note.settings import EMAIL_HOST_USER
from .models import Note, Contact
from django.contrib.auth import authenticate, login as userlogin, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# from . serializers import NoteSerializers
# from rest_framework import APIView
# from rest_framework.response import Response

# Create your views here.
def index(request):
    print(request.user)
    if(request.method=="POST"):
        if not request.user.is_authenticated:
            return redirect('/user_login')
        title = request.POST.get('title')
        note = request.POST.get('note')
        date = request.POST.get('date')
        data = Note(user=request.user,title=title,note=note,date=date)
        data.save()
    return render(request, 'index.html')

def register(request):
    if(request.method=="POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        num = request.POST.get('num')
        passwd = request.POST.get('passwd')
        pic = request.POST.get('pic')
        # data = Register(name=name,email=email,num=num,passwd=passwd)
        # data.save()
        # myuser = User.objects.create_user(name,email,passwd)
        myuser = User.objects.create_user(username=email,first_name=name,email=email,password=passwd)
        myuser.num = num
        myuser.pic = pic
        myuser.save()
        subject = 'Welcome email'
        message = 'You are successfully registered. Welcome to PNWAT Notes.'
        settings.EMAIL_HOST_USER
        send_mail(
        subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
        #messages.success(request, "Successfully Logged In")
        return redirect('/user_login')
    return render(request, 'register.html')

def user_login(request):
    if(request.method=="POST"):
        loginname = request.POST.get('loginname')
        loginpasswd = request.POST.get('loginpasswd')
        #print(loginname,loginpasswd)
        usr = authenticate(username=loginname, password=loginpasswd)
        #print(user)
        if usr is not None:
            userlogin(request, usr)
            return redirect('userpage')
            
        else:
            # messages.error(request, "Invalid Login Id or Password !")
            return HttpResponse('Invalid Credentials...!')

    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    return redirect('user_login')
@login_required(login_url='/user_login')
def task(request):
    if(request.method=="POST"):
        title = request.POST.get('title')
        note = request.POST.get('note')
        date = request.POST.get('date')
        data = Note(user=request.user,title=title,note=note,date=date)
        data.save()
    #usrid = request.User.user
    allNotes = Note.objects.filter(user=request.user)
    context = {'task':allNotes}
    return render(request, 'user.html', context)

def delete_note(request, myid):
    notes = Note.objects.filter(id=myid)
    notes.delete()
    return redirect('userpage')
    # notes = Note.objects.get(pk=id)
    # notes.delete()
    # return redirect('userpage')

def edit_note(request, myid):
    set_note = Note.objects.filter(id = myid)
    print(set_note)
    allNotes = Note.objects.filter(user=request.user)
    context = {'set_note':set_note, 'task':allNotes}
    return render(request, 'edit.html', context) 
    
@login_required()
def search(request):
    query = request.GET.get('query')
    task = Note.objects.filter(title=query)
    #task = Note.objects.all()
    print(task)
    params = {'task':task}
    return render(request, 'search.html', params)

def update_note(request, myid):
    note = Note.objects.get(id = myid)
    note.title = request.POST.get('title')
    note.note = request.POST.get('note')
    note.date = request.POST.get('date')
    note.save()
    #messages.info(request, "Note Updated Successfully...")
    return redirect('userpage')

def contact(request):
    if(request.method=="POST"):
        # if not request.user.is_authenticated:
        #     return redirect('/user_login')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        data = Contact(name=name,email=email,subject=subject,msg=msg)
        data.save()
    return render(request, 'Contact.html')

def aboutus(request):
    return render(request, 'about.html')

# class NoteList(APIView):
    
#     def get(self, request):
#         note1 = Note.objects.all()
#         serializer = NoteSerializers(note1, many=True)
#         return Response(serializer.data)

#     def post(self):
#         pass