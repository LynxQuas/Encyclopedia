from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry_page"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    path("edit/", views.edit, name="edit"),
    path("save/", views.save, name="save"),
    path("random/", views.random_page, name="random")
]
