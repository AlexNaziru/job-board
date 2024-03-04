from django.urls import path
from . import views


urlpatterns = [
    path('', views.BrowseJobsView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('newest/', views.NewJobView.as_view()),
    path('<int:pk>/', views.JobDetailView.as_view())
]