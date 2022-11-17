from django.shortcuts import render,redirect
from django.http import HttpResponse
from task.models import Task
from task.forms import TaskForm
# Create your views here.

def index(request):
    task = Task.objects.all()

    form = TaskForm()

    if request.method =="POST":
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/')    
    

    context = {'task' : task,'form':form}
    return render(request,'list.html',context)

def updateTask(request, pk):
    tasks = Task.objects.get(id=pk)    
    form = TaskForm(instance=tasks)

    if request.method =="POST":
        form = TaskForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'update_task.html',context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method =="POST":
        item.delete()
        return redirect("/")
    context = {'item':item}
    return render(request,'delete.html',context)


