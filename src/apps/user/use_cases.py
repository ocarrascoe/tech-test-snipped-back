from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from apps.user import serializers
from apps.user.repositories import UserRepository


class UserUseCases:

    def get_users(self):
        try:
            users = UserRepository.get_users()
            serialized_users = serializers.UserListSerializer(users, many=True).data
            return {'data': serialized_users, 'status': status.HTTP_200_OK}
        except ObjectDoesNotExist:
            return {'data': {'error': 'Books not found.'}, 'status': status.HTTP_404_NOT_FOUND}
