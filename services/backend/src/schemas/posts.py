from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Posts


PostInSchema = pydantic_model_creator(
    Posts, name="PostIn", exclude=["author_id"], exclude_readonly=True)
PostOutSchema = pydantic_model_creator(
    Posts, name="Post", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdatePost(BaseModel):
    title: Optional[str]
    content: Optional[str]
    category: Optional[str]