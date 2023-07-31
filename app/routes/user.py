from fastapi import APIRouter, Depends
from app.schemas.User import (
    CreateUserRes,
    Profile,
    ManyUserResponse,
)
from app.services.user import UserService
import logging
from app.dependencies import rate_limit


logger = logging.getLogger(__name__)


def create_user_router(profile_infos: dict, users_content: dict) -> APIRouter:
    user_router = APIRouter(
        prefix="/user",
        tags=["User"],
        dependencies=[Depends(rate_limit)]
    )
    user_service = UserService(profile_infos, users_content)

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


    @user_router.post("/", response_model=CreateUserRes, status_code=201)
    async def add_user(full_user_info: Profile):
        user_id = await user_service.create_update_user(full_user_info)
        return CreateUserRes(user_id=user_id)

    return user_router
