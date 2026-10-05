from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def register_and_login():
    email = "test_user_pocketsmart_qa@example.com"
    client.post("/register", json={
        "name": "Test User",
        "email": email,
        "password": "password123"
    })
    response = client.post("/login", json={
        "email": email,
        "password": "password123"
    })
    assert response.status_code in (200, 401)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_home():
    register_and_login()
    response = client.post("/generate-home", json={
        "budget": 20000,
        "room_type": "Living Room",
        "style": "Modern",
        "items": [{"name": "Ceiling Light", "quantity": 2}]
    })
    assert response.status_code == 200
    assert response.json()["planner"] == "home"
    assert response.json()["estimated_total"] <= 20000

def test_party():
    register_and_login()
    response = client.post("/generate-party", json={
        "budget": 30000,
        "guests": 30,
        "event_type": "Birthday",
        "venue": "Home",
        "preferences": "simple"
    })
    assert response.status_code == 200
    assert response.json()["planner"] == "party"
