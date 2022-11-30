"""Define main morale meter."""


from fastapi import FastAPI

from app.api import root, survey
from app.core import config

app = FastAPI(
    title="Morale Meter",
    description="A project to measure the team morale.",
    version="0.0.1",
    debug=config.DEBUG,
    redoc_url=None,
)

# Routers
# https://fastapi.tiangolo.com/tutorial/bigger-applications/#the-main-fastapi

app.include_router(root.router)
app.include_router(survey.router)
