from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout,login,authenticate
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class LoginView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return redirect('tasklist')
        else:
            msg=''
            return render(request,'login.html',{'msg':msg})

    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('tasklist')
        else:
            msg = "Invalid Credentials"
            return render(request,'login.html',{'msg':msg})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class CreateUser(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request,'create.html',{'form':form})

    def post(self,request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            msg ="Account created successfully.Please login"
            return render(request,'login.html',{'msg':msg})
        else:
            return render(request,'create.html',{'form':form})

class TaskList(View):
    def get(self,request):
        user = request.user
        task = Task.objects.filter(user=user)
        return render(request,'index.html',{'task':task,'user':user})

class AddTask(View):
    def get(self,request):
        form = TaskEditForm()
        return render(request,'addtask.html',{'form':form})

    def post(self,request):
        form = TaskEditForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tasklist')

class TaskDetail(View):
    def get(self,request,id):
        task = Task.objects.get(id=id)
        return render(request,'details.html',{'task':task,})

class EditTask(View):
    def get(self,request,id):
        task = Task.objects.get(id=id)
        form = TaskEditForm(instance=task)
        return render(request,'edit.html',{'form':form})

    def post(self,request,id):
        task = Task.objects.get(id=id)
        form = TaskEditForm(request.POST,instance=task)
        try:
            if form.is_valid():
                form.save()
                return redirect('tasklist')
        except:
            return HttpResponse("Saving failed")

class TaskDelete(View):
    def get(self,request,id):
        task = Task.objects.get(id=id)
        qns="Are you sure you want to delete this task?"
        return render(request,'confirmation.html',{'task':task,'qns':qns})

    def post(self,request,id):
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('tasklist')





