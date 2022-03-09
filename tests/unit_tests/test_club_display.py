import pytest
import server
from conftest import client
from server import showSummary, clubs, app



class TestDisplayClubs():
    """
        Testing the loging functions with pytest
    """    
    
    @pytest.fixture
    def clubs(self):
        """
            Clubs Fixture
        """
        return [{'name': 'Simply Lift', 'email': 'john@simplylift.co', 'points': '20'}, {'name': 'Iron Temple', 'email': 'admin@irontemple.com', 'points': '4'}, {'name': 'She Lifts', 'email': 'kate@shelifts.co.uk', 'points': '12'}]



    def test_display_clubs(self, client):
        """
            Should display a list of clubs when logged in
        """

        response = client.post('/showSummary',
                               data=dict(email="john@simplylift.co"),
                               follow_redirects=True
                               )
        html_response = response.data.decode()
        assert response.status_code == 200
        assert "Clubs:" in html_response
        assert "Simply Lift" in html_response


