from typing import List, Union

from fastapi import APIRouter
from api.db import models
from api.endpoints import schemas

patients_router = APIRouter()


@patients_router.post('/create', status_code=201, response_model=schemas.PatientId)
def create_patient(patient: schemas.PatientIn):
    patient_db = models.Patient.create(name_last=patient.name_last, name_first=patient.name_first,
                                       name_middle=patient.name_middle, birth_date=patient.birth_date)
    return schemas.PatientId(id=patient_db.id)


@patients_router.post('/registration', status_code=201,
                      response_model=Union[schemas.PatientId, schemas.Error, schemas.RegistrationId])
def create_registration(registration: schemas.RegistrationIn):
    if not models.Patient.select().where(models.Patient.id == registration.patient_id).exists():
        return schemas.Error(msg='Patient not found', code=1)
    if not models.Service.select().where(models.Service.id == registration.service_id).exists():
        return schemas.Error(msg='Service not found', code=2)
    registration_db = models.Registration.create(patient=registration.patient_id, service=registration.service_id,
                                                 date=registration.date)
    return schemas.RegistrationId(id=registration_db.id)


@patients_router.get('/registration', status_code=200,
                     response_model=Union[schemas.Error, List[schemas.RegistrationView]])
def get_registrations(patient: schemas.PatientId):
    if not models.Patient.select().where(models.Patient.id == patient.id).exists():
        return schemas.Error(msg='Patient not found', code=1)
    registrations = models.Registration.select().join(models.Service)\
        .where(models.Registration.patient == patient.id)
    return [schemas.RegistrationView(
        service=schemas.Service(id=registration.service.id, name=registration.service.name), date=registration.date)
        for registration in registrations]
