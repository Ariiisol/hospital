from typing import List

from fastapi import APIRouter
from api.db import models
from api.endpoints import schemas

services_router = APIRouter()


@services_router.get('/', status_code=200)
def get_services() -> List[schemas.Service]:
    services = models.Service.select()
    return [schemas.Service(name=service.name, id=service.id) for service in services]
