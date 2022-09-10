from django.http import JsonResponse

def get_routes(request):
    routes = [
        {'GET': '/api/projects/1' },
        {'GET': '/api/projects' },
        {'POST': '/api/projects' },

    ]

    return JsonResponse(routes, safe=False)