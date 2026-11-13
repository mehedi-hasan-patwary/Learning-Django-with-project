from django.urls import path
from tasks.views import manager_dashboard,user_dashboard,test_2,test_3,create_task
urlpatterns = [
 path('manager-dashboard/',manager_dashboard),
 path('user-dashboard/',user_dashboard),
 path('test_2/',test_2),
 path('test_3/',test_3),
 path('create-task/',create_task)

]

