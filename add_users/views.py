from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User


class AddUserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        if not username or not email:
            return Response({"error": "Username and email are required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create(username=username, email=email)
            return Response({"message": f"User {user.username} added successfully!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def sample_view(request):
    return JsonResponse({"message": "Hello from RepoA - Change 3 Friday"})