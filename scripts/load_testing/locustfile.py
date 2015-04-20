from locust import HttpLocust, TaskSet, task
import random


username = "demo"
password = "demo"


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/accounts/signin/", {"username": username, "password": password})

    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def drawings(self):
        self.client.get("/drawing/get_drawings")

    @task(3)
    def scenarios(self):
        self.client.get("/scenario/get_scenarios")

    @task(4)
    def filter_results(self):
        mindepth = (random.randint(0, 3) * 10) - 1
        maxdepth = random.randint(3, 10) * 10
        self.client.get("/scenario/get_filter_results"
                        "?depth_mean=true"
                        "&depth_mean_min=%d"
                        "&depth_mean_max=%d"
                        "&depth_mean_input=0" % (mindepth, maxdepth))


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
