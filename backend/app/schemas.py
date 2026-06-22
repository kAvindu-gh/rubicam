from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    model_config = {"from_attributes": True}


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut


class CubeSolveRequest(BaseModel):
    cube_state: str = Field(min_length=54, max_length=54, description="URFDLB notation string")
    save: bool = True


class CubeValidationOut(BaseModel):
    valid: bool
    errors: list[str] = []


class CubeSolveOut(BaseModel):
    valid: bool
    errors: list[str] = []
    solution: list[str] = []
    move_count: int = 0
    complexity: str = "unknown"


class SolveSessionOut(BaseModel):
    id: int
    cube_state: str
    solution: list[str]
    move_count: int
    complexity: str
    created_at: datetime


class AnalyticsOut(BaseModel):
    total_solved: int
    average_move_count: float
    best_move_count: int | None
    daily_streak: int

