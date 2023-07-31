from typing import Optional
from app.schemas.User import (
    Profile,
    User
)
from app.exceptions import UserNotFound

class UserService:

    def __init__(self, profile_infos: dict, users_content: dict):
        self.profile_infos = profile_infos
        self.users_content = users_content

    async def get_all_users_with_pagination(self, start: int, limit: int) -> tuple[list[Profile], int]:
        list_of_users = []

        keys = list(self.profile_infos.keys())

        total = len(keys)

        for index in range(len(keys)):
            if index < start:
                continue
            current_key = keys[index]
            user = await self.get_user_info(current_key)
            list_of_users.append(user)
            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    async def get_user_info(self, user_id: int = 0) -> Profile:
        if user_id not in self.profile_infos:
            raise UserNotFound(user_id=user_id)
        user_profile = self.profile_infos[user_id]
        user_content = self.users_content[user_id]

        user = User(**user_content)

        full_u_profile = {
            **user_profile,
            **user.dict()
        }

        return Profile(**full_u_profile)

    async def create_update_user(self, user_profile: Profile, user_id: Optional[int] = None) -> int:
        """
        Create user and new unique user id if not exist otherwise update the user.
        Placeholder implementation later to be update with DB.

        :param user_profile: Profile - User information saved in database.
        :param user_id: Optional[int] - user_id if already exists, otherwise to be set.
        :return user_id: int = existing or new user_id.
        """
        if user_id is None:
            user_id = len(self.profile_infos)
        liked_posts = user_profile.liked_posts
        shrt_desc = user_profile.short_description
        lng_bio = user_profile.long_bio

        self.users_content[user_id] = {"liked_posts": liked_posts}
        self.profile_infos[user_id] = {
            "short_description": shrt_desc,
            "long_bio": lng_bio
        }

        return user_id

    async def delete_user(self, user_id: int) -> None:
        if user_id not in self.profile_infos:
            raise UserNotFound(user_id=user_id)

        del self.profile_infos[user_id]
        del self.users_content[user_id]
