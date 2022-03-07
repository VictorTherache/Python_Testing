import pytest
import server
from conftest import client


class TestLoginWithDb():
    """
    Testing the 2 modules : JSON files and server.py login functions
    """

    def login_with_user_in_db():
        """
        This test is using a the first user
        in the db to login and should return
        a 200 response with the welcome
        page
        """
        clubs = server.loadClubs()
        print(clubs[0])
        login_response = client.post("/ShowSummary",
                                    data={
                                        "email": clubs[0]['name']
                                    },
                                    follow_redirects=True
                                    )
        html_response = login_response.data.decode()
        assert login_response.status_code == 200
        assert clubs[0]['name'] in html_response



