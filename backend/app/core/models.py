"""Define app models."""

from pydantic import BaseModel


class Survey(BaseModel):
    id: int
    vote: int
