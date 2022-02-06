from fastapi import APIRouter

from src.python.app.api.v1.home import router as home_router
from src.python.app.api.v1.login import router as login_router
from src.python.app.api.v1.tasks import router as tasks_router
from src.python.app.api.v1.users import router as users_router
from src.python.app.core.config import settings

router = APIRouter(prefix="/v1")
active_services = [key.strip().lower() for key in settings.ACTIVE_SERVICES.split(',')]

if('home' in active_services or 'all' in active_services):
    router.include_router(home_router)
if('login' in active_services or 'all' in active_services):
    router.include_router(login_router)
if('task' in active_services or 'all' in active_services):
    router.include_router(tasks_router)
if('users' in active_services or 'all' in active_services):
    router.include_router(users_router)