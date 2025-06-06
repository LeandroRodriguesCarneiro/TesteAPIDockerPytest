import json

def test_create_process(client):
    payload = {
        "name": "Processo teste"
    }

    response = client.post('/process/', data=json.dumps(payload), content_type="application/json")

    assert response.status_code == 201

    data = response.get_json()
    
    assert data["name"] == payload["name"]

def test_get_process(client):
    response = client.get("/process/")

    assert response.status_code == 200
    
    process = response.get_json()
    
    assert isinstance(process, list)
    assert len(process) >= 1