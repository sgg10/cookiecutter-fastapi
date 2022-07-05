from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.sample import router as SampleRouter
import app.core.settings as app_settings

app = FastAPI(prefix='')

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(SampleRouter)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {app_settings.app_name} | Version: {app_settings.version}"
    }

@app.get("/about")
def about():
    return app_settings.author
