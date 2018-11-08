from django.shortcuts import render
from django.http import JsonResponse
from .models import Project
from .serializers import ProjectSerializer




# Create your views here.
def home(request):
    if request.method == "GET":
        project_list = Project.objects
        serializer = ProjectSerializer(project_list, many = True)
        return JsonResponse(serializer.data, safe=False)
