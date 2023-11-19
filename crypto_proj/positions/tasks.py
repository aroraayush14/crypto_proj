from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab
from .models import Test  # Assuming Test is defined in the same module

app = Celery('crypto_proj')

# Your Celery configuration goes here...

@app.task
def create_test_job(name):
    Test.objects.create(name=name)

@periodic_task(run_every=crontab(minute='*/1'))
def run_create_objs():
    create_test_job.delay('new2023')
