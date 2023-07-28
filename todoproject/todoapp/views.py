from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'obj'

class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'tsk'






def index(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'obj':task1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'obj2':form,'obj3':task})



