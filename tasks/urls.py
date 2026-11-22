from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,test_2,test_3,create_task,create_task_2,view_task,view_task_2
urlpatterns = [
 path('manager-dashboard/',manager_dashboard),
 path('user-dashboard/',user_dashboard),
 path('test_2/',test_2),
 path('test_3/',test_3),
 path('create-task/',create_task),
 path("create-task-2/",create_task_2),
 path('view_task/',view_task),
 path('view_task_2/',view_task_2)

]

