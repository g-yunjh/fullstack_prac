from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.posts as crud
from src.auth.jwthandler import get_current_user
from src.schemas.posts import PostOutSchema, PostInSchema, UpdatePost
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()

@router.get(
    "/posts",
    response_model=List[PostOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_posts():
    return await crud.get_posts()

@router.get(
    "/posts/{category}",
    response_model=List[PostOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_posts_by_category(category: str) -> List[PostOutSchema]:
    try:
        return await crud.get_posts_by_category(category)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Category does not exist",
        )

@router.get(
    "/post/{post_id}",
    response_model=PostOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_post(post_id: int) -> PostOutSchema:
    try:
        return await crud.get_post(post_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Post does not exist",
        )

@router.get(
    "/post/{category}/{post_id}",
    response_model=PostOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_post_by_category_and_id(category: str, post_id: int) -> PostOutSchema:
    try:
        return await crud.get_post_by_category_and_id(category, post_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Post does not exist",
        )

@router.post(
    "/posts", response_model=PostOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_post(
    post: PostInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> PostOutSchema:
    return await crud.create_post(post, current_user)

@router.patch(
    "/post/{post_id}",
    dependencies=[Depends(get_current_user)],
    response_model=PostOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_post(
    post_id: int,
    post: UpdatePost,
    current_user: UserOutSchema = Depends(get_current_user)
) -> PostOutSchema:
    return await crud.update_post(post_id, post, current_user)

@router.delete(
    "/post/{post_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_post(
    post_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_post(post_id, current_user)
