import time
from locust import HttpUser, task
import json
import random

class QuickstartUser(HttpUser):
    Games = []
    with open('Games.json') as json_file:
        data = json.load(json_file)
        Games.extend(data)

    @task
    def insercion_game(self):
        time.sleep(3)
        response = self.client.post("/Games",json=random.choice(self.Games))
        print(response.json())