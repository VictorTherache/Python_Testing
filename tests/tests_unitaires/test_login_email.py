import pytest
import server
from conftest import client
from server import showSummary, clubs, app


def test_index_page_should_return_200(client):
    """
            Testing the status code of index page
    """
    response = client.get('/')
    assert response.status_code == 200


def test_unknown_page_should_return_404(client):
    """
            Testing the status code of an unknown page
    """
    response = client.get('/unknown_page')
    assert response.status_code == 404


class TestLoginEmail:
    """
        Testing the loging functions with pytest
    """
    @pytest.fixture
    def clubs(self):
        """
            Clubs Fixture
        """
        return [{'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': '13'}, {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': '4'}, {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': '12'}]


    @pytest.fixture
    def competitions(self):
        """
            Competitions fixture
        """
        return [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '25'}, {'name': 'Fall Classic', 'date': '2020-10-22 13:30:00', 'numberOfPlaces': '13'}]


    def test_right_email(self, client, clubs, mocker):
        """
            Should return response 200 with right email
        """

        mocker.patch.object(server, 'clubs', clubs)
        response = client.post('/showSummary',
                               data=dict(email="john@simplylift.co"),
                               follow_redirects=True
                               )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "Welcome" in html_response


    def test_wrong_email(self, client, clubs, mocker):
        """
            Should return a response 200 when providing wrong email
        """
        mocker.patch.object(server, 'clubs', clubs)
        response = client.post('/showSummary',
                              data=dict(email="wrong_email@mail.com"),
                              follow_redirects=True
                              )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "Incorrect email" in html_response
