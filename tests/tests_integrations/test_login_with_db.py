from re import T
import pytest
import server



@pytest.fixture
def client():
    """
    Setting up the client
    """
    server.app.config["TESTING"] = True
    client = server.app.test_client()
    return client


def test_login_with_db(client):
    """
    Testing the login with an email
    from the database
    """
    competitions = server.loadCompetitions()
    clubs = server.loadClubs()
    response = client.post("/showSummary",
                            data={
                                "email": clubs[0]['email']
                            },
                            follow_redirects=True
                            )
    html_response = response.data.decode()
    assert response.status_code == 200
    assert clubs[0]['email'] in html_response


    
    # club = server.clubs[0]
    # competition = server.competitions[0]

    # club_before_point = club["points"]
    # competition_before_place = competition['numberOfPlaces']
    # result_purchase_place = client.post("/purchasePlaces",
    #                                     data={
    #                                         "club": club["name"],
    #                                         "competition": competition["name"],
    #                                         "places": 10
    #                                     })
    # assert result_purchase_place.status_code == 200
    # assert club["points"] != club_before_point
    # assert competition["numberOfPlaces"] != competition_before_place

    # result_logout = client.get('/logout')
    # assert result_logout.status_code == 302