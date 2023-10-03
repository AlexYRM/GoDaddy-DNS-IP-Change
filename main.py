from apscheduler.schedulers.background import BackgroundScheduler
import write

# set up a blocking scheduler instance.
scheduler = BackgroundScheduler()

print("Start Scheduling jobs")
# add a job to the scheduler from "write" to be executed at 16:30 every day.
scheduler.add_job(func=write.ip_verification, trigger="cron", hour=16, minute=30)

# start the scheduler and run until requested to stop
scheduler.start()

# keep scheduler running until stopped manually
while True:
    pass
