def test_list_games(client):
    response = client.get('/games')
    assert response.status_code == 200

def test_add_game(client):
    response = client.post('/games', json={
        "title": "Test Game",
        "platform": "PC",
        "genre": "Strategy",
        "release_date": "2024-01-01"
    })
    assert response.status_code == 201
