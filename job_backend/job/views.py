from rest_framework import authentication, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategoriesSerializer


class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)

        return Response(serializer.data)


class NewJobView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)


class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        jobs = Job.objects.filter(created_by=request.user)
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)


class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        categories = request.GET.get("categories", "")
        query = request.GET.get("query", "")

        if query:
            jobs = jobs.filter(title__icontains=query)

        if categories:
            jobs = jobs.filter(category_id__in=categories.split(","))  # if the category is in the database, we filter it

        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)


class JobDetailView(APIView):
    def get(self, request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)

        return Response(serializer.data)

