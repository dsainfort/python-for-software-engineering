from pydantic import BaseModel, Field


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The username",
        description="This is the username of the user",
        min_length=1,
        max_length=20,
        default=None
    )
    
    liked_posts: list[int] = Field(
        description="Array of liked ids"
    )


class Profile(User):
    short_description: str
    long_bio: str


class ManyUserResponse(BaseModel):
    users: list[Profile]
    total: int


class CreateUserRes(BaseModel):
    user_id: int
    