import uvicorn
from fastapi import FastAPI

from routers import countries, storage, healthcheck
from config import settings

app = FastAPI()
app.include_router(countries.router, prefix="/v1")
app.include_router(storage.router, prefix="/v1")
app.include_router(healthcheck.router)


@app.on_event("startup")
def startup_event():
    # write logs
    pass


@app.on_event("shutdown")
def shutdown_event():
    # write logs
    pass


if __name__ == "__main__":
    uvicorn.run(app, host=settings.SERVER_HOST, port=int(settings.SERVER_PORT))
