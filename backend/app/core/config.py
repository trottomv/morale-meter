"""Define app config."""

import logging
import os

from app.core.commons import BooleanValue

try:
    from dotenv import find_dotenv, load_dotenv  # noqa
except ModuleNotFoundError:  # pragma: no cover
    pass
else:
    load_dotenv(find_dotenv())  # does not override already set variables

# Debug
DEBUG = BooleanValue.parse(os.getenv("DEBUG"))

# Environtment Configuration
CONFIGURATION = os.getenv("CONFIGURATION")

# API root URL path

API_ROOT: str = "/api"

# Surveys

SURVEYS = {
    "1": {"id": 1, "name": "Ownership & Empowerment", "slug": "ownership_empowerment"},
    "2": {"id": 2, "name": "Teamwork & Alignment", "slug": "teamwork_alignment"},
    "3": {"id": 3, "name": "Safety to take a risk", "slug": "safety_take_risk"},
    "4": {"id": 4, "name": "Pride", "slug": "pride"},
    "5": {"id": 5, "name": "Fun & Joy", "slug": "fun_joy"},
}

# Logging
try:
    logging.config.fileConfig(  # type: ignore
        "app/core/logging.conf",
        disable_existing_loggers=True,
    )
except AttributeError:  # pragma: no cover
    pass
log = logging.getLogger()
log.propagate = True

# Influxdb
try:
    import influxdb_client
except ModuleNotFoundError:
    influxdb_client = None
    pass
else:
    from influxdb_client.client.write_api import SYNCHRONOUS

    INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")
    INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")
    INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
    INFLUXDB_URL = os.getenv("INFLUXDB_URL")
    client = influxdb_client.InfluxDBClient(
        url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG
    )
    influxdb_write_api = client.write_api(write_options=SYNCHRONOUS)
