from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Task
from .forms import ManagerForm
from .forms import TaskForm
from django.http import HttpResponse
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Create your views here.

def task_pdf(request):
   buf = io.BytesIO()
   c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
   textob = c.beginText()
   textob.setTextOrigin(inch, inch)
   textob.setFont("Helvetica", 14)
   tasks = Task.objects.all()
   lines = []
   for task in tasks:
    lines.append(task.title)
    lines.append(task.status)
    lines.append(" ")
   for line in lines:
    textob.textLine(line)
   c.drawText(textob)
   c.showPage()
   c.save()
   buf.seek(0)
   return FileResponse(buf, as_attachment=True, filename='text.pdf')

def task_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=task.txt'
    tasks = Task.objects.all()
    lines = []
    for task in tasks:
        lines.append(f'{task.title}\n{task.manager}\n{task.due}\n{task.created}\n{task.priority}\n\n\n')

    response.writelines(lines)
    return response

def add_manager(request):
    submitted = False
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_manager?submitted=True')
    else:
         form = ManagerForm()
         if 'submitted' in request.GET:
               submitted = True
    return render(request, 'events/add_manager.html', {'form':form, 'submitted':submitted})
def add_task(request):
    submitted = False
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_task?submitted=True')
    else:
        form = TaskForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_task.html', {'form': form, 'submitted': submitted})
def all_tasks(request):
    task_list = Task.objects.all().order_by('-due', )
    #queryset = Task.objects.order_by('due')
    #form = TaskForm
    #if request.method == "POST":
        #form = TaskForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('/')
    return render(request, 'events/task_list.html', {'task_list': task_list})
def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
            form.save()
            return redirect('task-list')
    return render(request, 'events/update_task.html', {'task': task, 'form': form})
def list_task(request):
    task_list = Task.objects.all()
    return render(request, 'events/tasks.html', {'task_list': task_list})
#def show_task(request, Task_id):
  #  task = Task.objects.get(pk=Task_id)
  #  return render(request, 'events/show_task.html', {'task': task})
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('task-list')

def search_task(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        tasks = Task.objects.filter(title__contains=searched)
        return render(request, 'events/search_task.html', {'searched': searched, 'tasks': tasks})
    else:
        return render(request, 'events/search_task.html', {})


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "User"
    # لحتى فيي اكتب اول حرف من الشهر صغير
    month = month.title()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # Create Calender
    cal = HTMLCalendar().formatmonth(year, month_number)
    # Get current year
    now = datetime.now()
    current_year = now.year
    # Get current time
    time = now.strftime('%I :%M :%S %p')
    return render(request, 'events/home.html', {
                     "name": name,
                     "year": year,
                     "month": month,
                     "month_number": month_number,
                     "cal": cal,
                     "current_year": current_year,
                     "time": time
                     })

