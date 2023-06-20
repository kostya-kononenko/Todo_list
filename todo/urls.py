from django.urls import path

from .views import TagListView
from todo.views import (
    index,
    TaskCreateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskUpdateView,
    TaskDeleteView,
    complete_or_undo_task,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/",
         TaskCreateView.as_view(),
         name="task-create"),

    path("<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),

    path("<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),

    path("tags/",
         TagListView.as_view(),
         name="tag-list"),

    path("tags/create/",
         TagCreateView.as_view(),
         name="tag-create"),

    path("tags/<int:pk>/update/",
         TagUpdateView.as_view(),
         name="tag-update"),

    path("tags/<int:pk>/delete/",
         TagDeleteView.as_view(),
         name="tag-delete"),

    path(
        "tasks/complete/<int:pk>/",
        complete_or_undo_task,
        name="complete-or-undo-task"
    ),
]

app_name = "todo"
