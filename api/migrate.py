from api import config
from api.db.models import sqlite_db, Patient, Service, Registration

with sqlite_db:
    sqlite_db.create_tables([Patient, Service, Registration])

services = config.SERVICES_FILE.open().read().split('\n')
with sqlite_db:
    for service_name in services:
        Service.create(name=service_name)
