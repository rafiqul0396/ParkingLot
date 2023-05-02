from django.test import TestCase


import sched, time

def do_something(scheduler):
    # schedule the next call first
    scheduler.enter(60, 1, do_something, (scheduler,))
    print("Doing stuff...")
    # then do your stuff

my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(60, 1, do_something, (my_scheduler,))
my_scheduler.run()
# Create your tests here.
