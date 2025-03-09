from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    username: str | None
    first_name: str
    last_name: str | None
