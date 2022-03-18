from locust import HttpUser, task

import server

class WebPageTest(HttpUser):

    clubs = server.loadClubs()
    competitions = server.loadCompetitions()
    club = clubs[0]
    competition = competitions[2]


    def on_start(self):
        self.client.post(
            "/showSummary",
            {
                "email": self.club['email'],
            })


    @task
    def index(self):
        self.client.get("/")

    @task
    def book(self):
        self.client.get(
            "/book/" + self.competition['name'] + "/" + self.club['name']
            )

    @task
    def purchase_places(self):
        self.client.post(
            "/purchasePlaces",
            {
                "club": self.club['name'],
                "competition": self.competition['name'],
                "places": "0"
            }
        )

    @task
    def on_stop(self):
        self.client.get('/logout')  