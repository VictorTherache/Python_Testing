import pytest
import server
from conftest import client
from server import showSummary, clubs, app


class TestBooking:
    """
        Testing the booking functions with pytest
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


    def test_book_with_more_points_than_the_club_have(self, client, clubs, competitions, mocker):
        """
            Should return a error message saying that the club doesnt have
            enough points
        """

        response = client.post('/purchasePlaces',
                                data={'places':"14", 'competition': competitions[0]['name'], 'club': clubs[0]['name']})
        html_response = response.data.decode()
        print('test test')
        print(response.data)
        assert response.status_code == 200
        assert "Welcome" in html_response