from psycopg2 import ProgrammingError

from logger import logger

from database import BaseSystem
from .models import User


class UserSystem(BaseSystem):
    def __init__(self) -> None:
        super().__init__()
    
    def get_by_id(self, user_id: int):
        user = self.session.query(User) \
                            .filter_by(id=user_id) \
                            .first()
        return user        

    def get_by_username(self, username: str):
        user = self.session.query(User) \
                        .filter_by(username=username) \
                        .first()
        
        return user

    def create(self, user: User):
        db_user = self.session.query(User) \
                            .filter_by(id=user.id) \
                            .first()
        
        if db_user:
            logger.debug(f'Role {db_user.id} already exists.')
            return False
        
        try:
            self.session.add(user)
            self.session.commit()
        except ProgrammingError as e:
            logger.error(e)
            return False
        
        return True

user_system = UserSystem()
