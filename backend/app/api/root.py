"""Define app root endpoint."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """Define root endpoint."""
    return {
        "title": "Morale Meter",
        "description": "This app is a backend for measure team morale.",
    }
