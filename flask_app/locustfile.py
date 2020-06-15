"""Import locust"""
from locust import HttpUser, TaskSet, between

@task
def index_page(self):
    self.client.get("/")

class UserBehavior(TaskSet):
    """Define taskset"""
    tasks = {index : 1}

class WebsiteUser(HttpUser):
    """WebsiteUser simulation"""
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
