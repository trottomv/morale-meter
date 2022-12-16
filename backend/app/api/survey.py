"""Define app root endpoint."""

from datetime import datetime
from typing import Any, Dict, List

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from influxdb_client import Point, WritePrecision

from app.core import config, models

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get(f"{config.API_ROOT}/survey/")
async def survey():
    """Define the survey list endpoint."""
    return [config.SURVEYS[key] for key in config.SURVEYS.keys()]


@router.post(f"{config.API_ROOT}/survey/vote/")
async def vote_survey(surveys: List[models.Survey]) -> Dict[str, Any]:
    """Define the vote survey endpoint."""
    for survey in surveys:
        record = (
            Point(config.SURVEYS[str(survey.id)]["name"])
            .field("vote", survey.vote)
            .time(datetime.utcnow(), WritePrecision.NS)
        )
        config.influxdb_write_api.write(
            bucket=config.INFLUXDB_BUCKET, org=config.INFLUXDB_ORG, record=record
        )
    return {"detail": "Ok!"}


@router.get("/survey/")
async def survey_page(request: Request):
    return templates.TemplateResponse("survey.html", {"request": request})
