# portfolio/urls.py
from django.urls import path
from .views import HomeView, AboutView, ContactCreateView, ProjectListView, ProjectCreateView

urlpatterns = [
    path("home/", HomeView.as_view(), name="api-home"),
    path("about/", AboutView.as_view(), name="api-about"),
    path("contact/", ContactCreateView.as_view(), name="api-contact"),
    path("projects/", ProjectListView.as_view(), name="api-projects"),
    path("projects/create/", ProjectCreateView.as_view(), name="api-project-create"),
]