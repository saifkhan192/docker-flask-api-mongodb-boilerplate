
def test_get_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_put_survey(client):
    payload = dict(
        name = "Saifullah Khan",
        position = "Fullstack Software Engineer",
        feedback = "Very satisfied",
    )
    response = client.put("/api/survey", data = payload)
    assert b"Your survey has been received" in response.data

def test_get_survey(client):
    response = client.get("/api/survey")
    survey = response.json[0]
    assert 'name' in survey
    assert 'position' in survey
    assert 'feedback' in survey
    assert 'created_at' in survey