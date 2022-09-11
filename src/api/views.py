from django.http import HttpRequest

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProjectSerializer
from projects.services.projects import get_projects, get_project


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/projects/1' },
        {'GET': '/api/projects' },
        {'POST': '/api/projects' },

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'}

    ]

    return Response(routes) 


@api_view(['GET'])
def get_projects_api(request: HttpRequest):
    projects = get_projects()
    serializers = ProjectSerializer(projects, many=True)
    return Response(serializers.data, status=200)


@api_view(['GET'])
def get_project_api(request: HttpRequest, pk):
    project = get_project(pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data, status=200)