from api import config
import uuid
from peewee import Model, CharField, SqliteDatabase, DateTimeField, ForeignKeyField

sqlite_db = SqliteDatabase(config.DB_FILE, pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    class Meta:
        database = sqlite_db


class Patient(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    name_last = CharField()
    name_first = CharField()
    name_middle = CharField(null=True)
    birth_date = DateTimeField()


class Service(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    name = CharField()


class Registration(BaseModel):
    id = CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    patient = ForeignKeyField(Patient)
    service = ForeignKeyField(Service)
    date = DateTimeField()


