from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee, Task, TaskDetail, Project
# from tasks.models import *
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg


# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test_2(request):
    return render(request,'test_2.html')

def test_3(request):
    names = ["Mahmud", "Ahamed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test_3.html', context)


def create_task(request):
    return render(request,'task_form.html')

def create_task_2(request):
    # employees=Employee.objects.all()
    form=TaskModelForm()


    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'task_4.html', {"form": form, "message": "task added successfully"})





    context={"form":form}
    return render(request,'task_4.html',context)


def view_task(request):
    #getting all data
    tasks=Task.objects.all()
   #for a specific task
    task_3=Task.objects.get(id=1)

    first_task=Task.objects.first()
    pending_task_1=Task.objects.filter(status='PENDING')
    return render(request, "show_task.html", {"tasks": tasks,"task3":task_3,"first_task":first_task,"task_4":pending_task_1})


# def view_task_3(request):
#     pending_task_1=Task.objects.filter(status='PENDING')
#     return render(request, "show_task.html", {"tasks_4":pending_task_1})


#filter
def view_task_2(request):
    pending_task=Task.objects.filter(status='PENDING')
    return render(request, "show_task_2.html", {"tasks_5":pending_task})


def view_task_3(request):
    """Show the task that contain word paper"""
    tasks=Task.objects.filter(title_icontains="paper")
    return render(request, "show_task_2.html", {"tasks_6":tasks})
