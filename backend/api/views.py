from django.http import HttpRequest

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from api.serializers import ProjectSerializer
from projects.services.projects import get_projects, get_project, get_or_create_review
from projects.models import Tag


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
# @permission_classes([IsAuthenticated])
def get_projects_api(request: HttpRequest):
    print(request.user,'User --------------------------------')
    projects = get_projects()
    serializers = ProjectSerializer(projects, many=True)
    return Response(serializers.data, status=200)


@api_view(['GET'])
def get_project_api(request: HttpRequest, pk):
    project = get_project(pk)
    serializer = ProjectSerializer(project, many=False)

    return Response(serializer.data, status=200)
 

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_project_vote(request: HttpRequest, pk):
    project = get_project(pk)
    user = request.user.profile
    data = request.data

    review, created = get_or_create_review(pk, user, project)
    review.value = data['value']
    review.save()
    project.get_vote_count
    
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data) 

@api_view(['DELETE'])
def delete_tag(request: HttpRequest):
    pk = request.data['projectId']
    tag = request.data['tagId']

    project = get_project(pk)
    tag = Tag.objects.get(id = tag)
    
    project.tags.remove(tag)

    return Response("Tag was deleted")
     