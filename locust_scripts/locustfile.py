import random

import math
from locust import HttpLocust, TaskSet, task

Names = "Beatrix,Blaire,Callie,Cecily,Cleo,Coco,Cosette,Cybil,Daisy".split(",")
# load user credentials from CSV
#user_credentials = read_user_credentials_from_csv()
class WebsiteTasks(TaskSet):
    def on_start(self):
        # credentials = random.choice(user_credentials)
        # self.client.post("/login/", {"username":credentials[0], "password":credentials[1]})
        pass

    @task(1)
    def index(self):
        self.client.get("/")
        # self.client.get("/api1")

    @task
    def api1(self):
        self.client.get("/api1")
    @task
    def api2(self):
        self.client.get("/api2")
    @task
    def api3(self):
        self.client.get("/api3")

    @task
    def json_log(self):
        time_usage = math.fabs( random.normalvariate(4.01, 32.44))
        lat, lng = random.uniform(-180, 180), random.uniform(-90, 90)
        module = random.choice(Names)
        random_json = {
            "module":module,
            "lat":lat,
            "lng":lng,
            "time_usage":time_usage,
        }
        self.client.post("/json_log",json = random_json)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #By default the time is randomly chosen uniformly between min_wait and max_wait
    min_wait = 100
    max_wait = 1500