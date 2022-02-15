import pytest
import server
from conftest import client
from server import showSummary, clubs, app
from flask import Flask


class TestBooking():
    """
        Testing the booking functions with pytest
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
        return [{'name': 'Spring Festival', 'date': '2020-03-27 10:00:00', 'numberOfPlaces': '25'}, {'name': 'Fall Classic', 'date': '2020-10-22 13:30:00', 'numberOfPlaces': '13'}]


    def test_book_with_more_points_than_the_club_have(self, client, clubs, competitions, mocker):
        """
            Should return a error message saying that the club doesnt have
            enough points
        """
        response = client.post('/purchasePlaces',
                                data={'places':"21", 
                                      'competition': competitions[0]['name'],
                                      'club': clubs[0]['name']},
                                      follow_redirects=True
                                      )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "You can't book more places than the points you have!" in html_response


    def test_book_with_allowed_number_of_points(self, client, clubs, competitions, mocker):
        """
            Should return a 200 response and leads to the homepage
        """
        response = client.post('/purchasePlaces',
                                data={'places':"9", 
                                      'competition': competitions[0]['name'], 
                                      'club': clubs[0]['name']},
                                      follow_redirects=True)
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "Welcome" in html_response


    def test_book_with_more_than_12_points(self, client, clubs, competitions, mocker):
        """
            Should return a error message saying that the club cannot
            book more than 12 places
        """
        response = client.post('/purchasePlaces',
                                data={'places':"13", 'competition': competitions[0]['name'], 'club': clubs[0]['name']})
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "You can't book more than 12 places!" in html_response


    # def test_club_points_are_substracted_when_booking(self, client, clubs, competitions, mocker):
    #     """
    #         The clubs points should be substracted with the number
    #         of places chose when booking
    #     """
    #     response = client.post('/purchasePlaces',
    #                             data={'places':"5", 'competition': competitions[0]['name'], 'club': clubs[0]['name']})
    #     html_response = response.data.decode()
    #     assert response.status_code == 200
    #     assert "You can't book more places than the points you have" in html_response
