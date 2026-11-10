from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public view accessible to every one."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({"message":f"Hello, {request.user.username}. This is private "})