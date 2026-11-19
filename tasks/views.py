from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Employee,Task

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


            
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')  # list [1,3]

            # task = Task.objects.create(
            #     title=title, description=description, due_date=due_date)

            # # Assign employee to tasks
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)

            # return HttpResponse("Task Added successfully")



    context={"form":form}
    return render(request,'task_4.html',context)
  