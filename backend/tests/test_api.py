"""Define tests for main app."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    """Test root path."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["title"] == "Morale Meter"


def test_surey_list():
    """Test GET on survey list endpoint."""
    response = client.get("/api/survey/")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "name": "Ownership & Empowerment", "slug": "ownership_empowerment"},
        {"id": 2, "name": "Teamwork & Alignment", "slug": "teamwork_alignment"},
        {"id": 3, "name": "Safety to take a risk", "slug": "safety_take_risk"},
        {"id": 4, "name": "Pride", "slug": "pride"},
        {"id": 5, "name": "Fun & Joy", "slug": "fun_joy"},
    ]


def test_surey_vote():
    """Test POST on survey vote endpoint."""
    response = client.post(
        "/api/survey/vote/",
        json=[
            {"id": 1, "vote": 4},
            {"id": 2, "vote": 2},
            {"id": 3, "vote": 1},
            {"id": 4, "vote": 3},
            {"id": 5, "vote": 2},
        ],
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "Ok!"}
