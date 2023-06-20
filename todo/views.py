from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tag


def index(request):
    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks": tasks,
        "tags_list": tags,
    }

    return render(request, "todo/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def complete_or_undo_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.done_mark:
        task.done_mark = False
    else:
        task.done_mark = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))
