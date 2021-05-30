from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, constr


class PatientIn(BaseModel):
    name_last: str
    name_first: str
    name_middle: Optional[str]
    birth_date: datetime


class PatientId(BaseModel):
    id: UUID


class Service(BaseModel):
    id: UUID
    name: str


class RegistrationIn(BaseModel):
    patient_id: str
    service_id: str
    date: datetime


class RegistrationId(BaseModel):
    id: UUID


class RegistrationView(BaseModel):
    service: Service
    date: datetime


class Error(BaseModel):
    msg: str
    code: int

