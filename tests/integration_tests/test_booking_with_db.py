import pytest
import server
from conftest import client
from server import showSummary, clubs, app
from flask import Flask


class TestBookingUsingDb():
    """
        Testing the booking functions with pytest
    """


    def test_book_using_correct_db_data(self, client):
        """
            This test books a competion using the JSON data.
            Should return a 200 response and redirect to homepage
        """
        clubs = server.loadClubs()
        competitions = server.loadCompetitions()

        response = client.post('/purchasePlaces',
                                data={'places':"1", 
                                      'competition': competitions[2]['name'],
                                      'club': clubs[0]['name']},
                                      follow_redirects=True
                                      )
        html_response = response.data.decode()

        assert response.status_code == 200
        assert "Great-booking complete!" in html_response


    def test_booking_too_much_places_and_using_db_data(self, client):
        """
            Should return a error message saying that the club doesnt have
            enough points
        """
        clubs = server.loadClubs()
        competitions = server.loadCompetitions()

        response = client.post('/purchasePlaces',
                                data={'places':"21", 
                                      'competition': competitions[0]['name'],
                                      'club': clubs[0]['name']},
                                      follow_redirects=True
                                      )

        html_response = response.data.decode()
        assert response.status_code == 200
        assert "You can't book more places than the points you have!" in html_response


    def test_club_points_are_substracted_when_booking_using_db_data(self, client):
        """
            The clubs points should be substracted with the number
            of places chose when booking
        """

        clubs = server.loadClubs()
        competitions = server.loadCompetitions()
        response = client.post('/purchasePlaces',
                                data={'places':"5",
                                      'competition': competitions[2]['name'],
                                      'club': clubs[0]['name']},
                                      follow_redirects=True
                                      )
        html_response = response.data.decode()
        print(html_response)
        assert response.status_code == 200
        assert "Points available: 7" in html_response


    def test_cant_book_past_competitions(self, client):
        """
            The clubs cannot book a competition if it already happened and
            should display an error message
        """
        clubs = server.loadClubs()
        competitions = server.loadCompetitions()
        response = client.post('/purchasePlaces',
                                data={'places':"5",
                                      'competition': competitions[1]['name'],
                                      'club': clubs[0]['name']},
                                      follow_redirects=True
                                      )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "This competition has already happened! Please book an upoming event" in html_response 
