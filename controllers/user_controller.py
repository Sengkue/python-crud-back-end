# controllers/user_controller.py
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.user import User
from schemas.user_schemas import UserCreate, UserUpdate
from typing import List, Optional
import hashlib

class UserController:
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password using SHA256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password"""
        return UserController.hash_password(plain_password) == hashed_password
    
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        """Create a new user"""
        try:
            # Hash the password
            hashed_password = UserController.hash_password(user_data.password)
            
            # Create user object
            db_user = User(
                username=user_data.username,
                email=user_data.email,
                password=hashed_password,
                first_name=user_data.first_name,
                last_name=user_data.last_name,
                phone=user_data.phone,
                bio=user_data.bio
            )
            
            # Add to database
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            
            return db_user
            
        except IntegrityError as e:
            db.rollback()
            if "username" in str(e.orig):
                raise ValueError("Username already exists")
            elif "email" in str(e.orig):
                raise ValueError("Email already exists")
            else:
                raise ValueError("User creation failed")
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """Get user by username"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """Get all users with pagination"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserUpdate) -> Optional[User]:
        """Update user"""
        try:
            db_user = db.query(User).filter(User.id == user_id).first()
            
            if not db_user:
                return None
            
            # Update fields if provided
            update_data = user_data.model_dump(exclude_unset=True)
            
            for field, value in update_data.items():
                setattr(db_user, field, value)
            
            db.commit()
            db.refresh(db_user)
            
            return db_user
            
        except IntegrityError as e:
            db.rollback()
            if "username" in str(e.orig):
                raise ValueError("Username already exists")
            elif "email" in str(e.orig):
                raise ValueError("Email already exists")
            else:
                raise ValueError("User update failed")
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """Delete user"""
        db_user = db.query(User).filter(User.id == user_id).first()
        
        if not db_user:
            return False
        
        db.delete(db_user)
        db.commit()
        
        return True
    
    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
        """Authenticate user"""
        user = UserController.get_user_by_username(db, username)
        
        if not user:
            return None
            
        if not UserController.verify_password(password, user.password):
            return None
            
        return user