from src.python.app.crud.base import CRUDBase
from src.python.app.models.users import User
from src.python.app.schemas.user import UserInDB, UserUpdateDB

CRUDUser = CRUDBase[User, UserInDB, UserUpdateDB]
crud_user = CRUDBase(User)