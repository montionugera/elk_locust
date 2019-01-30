from locust import HttpLocust, TaskSet, task


# load user credentials from CSV
#user_credentials = read_user_credentials_from_csv()
class WebsiteTasks(TaskSet):
    def on_start(self):
        # credentials = random.choice(user_credentials)
        # self.client.post("/login/", {"username":credentials[0], "password":credentials[1]})
        pass

    @task(10)
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


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    #By default the time is randomly chosen uniformly between min_wait and max_wait
    min_wait = 100
    max_wait = 1500