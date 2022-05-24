from typing import List

from apps.user.models import User


class UserRepository:
    @staticmethod
    def get_users() -> List[User]:
        return User.objects.all()