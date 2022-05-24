from rest_framework.response import Response
from rest_framework.views import APIView

from apps.user.use_cases import UserUseCases


class UserListView(APIView):
    # Get all users
    def get(self, format=None):
        response = UserUseCases().get_users()
        return Response(response['data'], status=response['status'])