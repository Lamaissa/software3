from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_tasks, name="task-list"),
    path('add_manager', views.add_manager, name="add-manager"),
    path('add_task', views.add_task, name="add-task"),
    path('tasks', views.list_task, name="list-task"),
    path('update_task/<task_id>/', views.update_task, name="update-task"),
    path('search_task', views.search_task, name="search-task"),
    path('delete_task/<task_id>/', views.delete_task, name="delete-task"),
    path('task_text', views.task_text, name="task_text"),
    path('task_pdf', views.task_pdf, name="task-pdf"),
   # path('show_task/<Task_id>/', views.show_task, name="show-task"),

]
