from fastapi import APIRouter
from app.schemas.User import (
    CreateUserRes,
    Profile,
    ManyUserResponse,
)
from app.services.user import UserService


def create_user_router() -> APIRouter:
    user_router = APIRouter(
        prefix="/user",
        tags=["User"]
    )
    user_service = UserService()

    @user_router.get("/all", response_model=ManyUserResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_all_users_with_pagination(start, limit)
        formatted_users = ManyUserResponse(users=users, total=total)
        return formatted_users

    @user_router.get("/{user_id}", response_model=Profile)
    async def get_user_by__id(user_id: int):
        """
        Endpoint for retrieving a full user profile byt the user's unique ID.

        :param user_id: int - unique monotonically increasing integer id
        :return: FullUserProfile
        """
        user_profile = await user_service.get_user_info(user_id)
        return user_profile


    @user_router.put("/{user_id}")
    async def update_user(user_id: int, full_user_info: Profile):
        await user_service.create_update_user(full_user_info, user_id)
        return None


    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int):
        await user_service.delete_user(user_id)

    @user_router.post("/", response_model=CreateUserRes)
    async def add_user(full_user_info: Profile):
        user_id = await user_service.create_update_user(full_user_info)
        return CreateUserRes(user_id=user_id)

    return user_router
