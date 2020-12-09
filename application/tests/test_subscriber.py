
def test_get_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_put_survey(client):
    subscriber = {
        'name': "Saifullah Khan",
        'email': "saifkhan912@gmail.com"
    }
    response = client.post("/api/subscriber", data = subscriber)
    assert b"Thank you for subscribing" in response.data

def test_get_survey(client):
    response = client.get("/api/subscriber")
    response = response.data
    assert b"subscribers" in response