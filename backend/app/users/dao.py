from loguru import logger
from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.users.models import User

class UserDAO(BaseDAO):
    model = User
