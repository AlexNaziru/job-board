from django.urls import path
from . import views


urlpatterns = [
    path('newest/', views.NewJobView.as_view()),
    path('<int:pk>/', views.JobDetailView.as_view())
]