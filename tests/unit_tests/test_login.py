import pytest
import server
from conftest import client
from server import showSummary, clubs, app



class TestLoginEmail():
    """
        Testing the loging functions with pytest
    """    
    
    @pytest.fixture
    def clubs(self):
        """
            Clubs Fixture
        """
        return [{'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': '20'}, {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': '4'}, {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': '12'}]


    @pytest.fixture
    def competitions(self):
        """
            Competitions fixture
        """
        return [{'name': 'Spring Festival', 'date': '2022-05-27 10:00:00', 'numberOfPlaces': '25'}, {'name': 'Fall Classic', 'date': '2020-10-22 13:30:00', 'numberOfPlaces': '13'}]


    def test_display_right_data_when_login(self, client):
        """
            Should display the right username and list of clubs when logging in
        """

        response = client.post('/showSummary',
                               data=dict(email="john@simplylift.co"),
                               follow_redirects=True
                               )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "john@simplylift.co" in html_response


    def test_wrong_email(self, client):
        """
            Should return a response 200 when providing wrong email
        """
        response = client.post('/showSummary',
                              data=dict(email="wrong_email@mail.com"),
                              follow_redirects=True
                              )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "Incorrect email" in html_response
