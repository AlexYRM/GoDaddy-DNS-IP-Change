from apscheduler.schedulers.background import BlockingScheduler
import write
import time

# set up a blocking scheduler instance.
scheduler = BlockingScheduler()

print("Start Scheduling jobs")
# add a job to the scheduler from "write" to be executed at 09:20 every day.
scheduler.add_job(func=write.ip_verification, trigger="cron", hour=17, minute=59)

# start the scheduler and run until requested to stop
scheduler.start()

# # keep scheduler running until stopped manually
# while True:
#     time.sleep(2)
