from rest_framework.decorators import api_view
from rest_framework.response import Response


# The code taken from the Code Institute drf-api project
@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to drf API!"
    })