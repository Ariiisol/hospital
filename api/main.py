import uvicorn
from fastapi import FastAPI

from api.endpoints.patients_router import patients_router
from api.endpoints.services_router import services_router

app = FastAPI()
app.include_router(
    patients_router,
    prefix='/patients'
)

app.include_router(
    services_router,
    prefix='/services'
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
