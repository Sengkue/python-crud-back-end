# schemas/user_schemas.py
from pydantic import BaseModel, validator, Field
from typing import Optional
from datetime import datetime
import re

class UserBase(BaseModel):
    username: str = Field(..., example="johndoe")
    email: str = Field(..., example="john@example.com")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    phone: Optional[str] = Field(None, example="+1234567890")
    bio: Optional[str] = Field(None, example="Hello, I'm John!")
    
    @validator('username')
    def validate_username(cls, v):
        if len(v) < 3:
            raise ValueError('Username must be at least 3 characters long')
        if len(v) > 50:
            raise ValueError('Username must be less than 50 characters')
        return v
    
    @validator('email')
    def validate_email(cls, v):
        # Simple email validation using regex
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, v):
            raise ValueError('Invalid email format')
        return v

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, example="password123")
    
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters long')
        return v

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, example="johndoe_updated")
    email: Optional[str] = Field(None, example="john.updated@example.com")
    first_name: Optional[str] = Field(None, example="Johnny")
    last_name: Optional[str] = Field(None, example="Doe")
    phone: Optional[str] = Field(None, example="+1987654321")
    bio: Optional[str] = Field(None, example="Updated bio text")
    is_active: Optional[bool] = Field(None, example=True)
    is_verified: Optional[bool] = Field(None, example=False)
    
    @validator('username')
    def validate_username(cls, v):
        if v is not None:
            if len(v) < 3:
                raise ValueError('Username must be at least 3 characters long')
            if len(v) > 50:
                raise ValueError('Username must be less than 50 characters')
        return v
    
    @validator('email')
    def validate_email(cls, v):
        if v is not None:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, v):
                raise ValueError('Invalid email format')
        return v

class UserResponse(UserBase):
    id: int
    is_active: bool
    is_verified: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str = Field(..., example="johndoe")
    password: str = Field(..., example="password123")