from django.http import JsonResponse

def get_routes(request):
    routes = [
        {'GET': '/api/projects/1' },
        {'GET': '/api/projects' },
        {'POST': '/api/projects' },

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'}

    ]

    return JsonResponse(routes, safe=False)