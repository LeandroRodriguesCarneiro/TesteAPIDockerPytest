import json

def test_create_log(client):
    payload = {
        "id_process": 1,
        "status_code": 200,
        "message": "Log de teste"
    }

    response = client.post("/logs/", data=json.dumps(payload), content_type="application/json")
    
    assert response.status_code == 201
    data = response.get_json()
    assert data["id_process"] == payload["id_process"]
    assert data["status_code"] == payload["status_code"]
    assert data["message"] == payload["message"]

def test_get_logs(client):
    response = client.get("/logs/")
    assert response.status_code == 200
    logs = response.get_json()
    assert isinstance(logs, list)
    assert len(logs) >= 1
