from psycopg2 import ProgrammingError

from logger import logger

from database import BaseSystem
from .models import Role


class RoleSystem(BaseSystem):
    def __init__(self) -> None:
        super().__init__()

    def create_role(self, role: Role):
        db_role = self.session.query(Role) \
                      .filter_by(id=role.id).first()
        
        if db_role:
            logger.debug(f'Role {db_role.id} already exists.')
            return False
        
        try:
            self.session.add(role)
            self.session.commit()
        except ProgrammingError:
            return False
        
        return True

    def update_role(self, id: int, role: Role):
        db_role = self.session.query(Role) \
                      .filter_by(id=id).first()

        if not db_role:
            logger.debug(f'Role {db_role.id} not exists.')
            return False
        
        try:
            self.session.query(Role).filter(Role.id == id).update({
                Role.name : Role.name
            }, synchronize_session=False)
            self.session.commit()
        except ProgrammingError as e:
            logger.debug(e)
            return False
        
        return True

role_system = RoleSystem()