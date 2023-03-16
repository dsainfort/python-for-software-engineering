from typing import Optional
from app.schemas.User import (
    Profile,
    User
)

profile_infos = {
    0: {
        "short_description": "Bio description",
        "long_bio": "More detailed information"
    }
}

users_content = {
    0: {
        "liked_posts": [1] * 9,
    }
}


class UserService:

    def __init__(self):
        pass

    async def get_all_users_with_pagination(self, start: int, limit: int) -> tuple[list[Profile], int]:
        list_of_users = []

        keys = list(profile_infos.keys())

        total = len(keys)

        for index in range(0, len(keys)):
            if index < start:
                continue
            current_key = keys[index]
            user = await self.get_user_info(current_key)
            list_of_users.append(user)
            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    @staticmethod
    async def get_user_info(user_id: int = 0) -> Profile:

        user_profile = profile_infos[user_id]
        user_content = users_content[user_id]

        user = User(**user_content)

        full_u_profile = {
            **user_profile,
            **user.dict()
        }

        return Profile(**full_u_profile)

    @staticmethod
    async def create_update_user(user_profile: Profile, user_id: Optional[int] = None) -> int:
        """
        Create user and new unique user id if not exist otherwise update the user.
        Placeholder implementation later to be update with DB.

        :param user_profile: Profile - User information saved in database.
        :param user_id: Optional[int] - user_id if already exists, otherwise to be set.
        :return user_id: int = existing or new user_id.
        """
        global profile_infos
        global users_content

        if user_id is None:
            user_id = len(profile_infos)
        liked_posts = user_profile.liked_posts
        shrt_desc = user_profile.short_description
        lng_bio = user_profile.long_bio

        users_content[user_id] = {"liked_posts": liked_posts}
        profile_infos[user_id] = {
            "short_description": shrt_desc,
            "long_bio": lng_bio
        }

        return user_id

    @staticmethod
    async def delete_user(user_id: int) -> None:
        global profile_infos
        global users_content

        del profile_infos[user_id]
        del users_content[user_id]
