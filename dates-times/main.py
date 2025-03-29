import datetime

date = datetime.date(2023, 12, 12)
today = datetime.date.today()
time = datetime.time(12, 30, 12)
nowTime = datetime.datetime.now()

now = nowTime.strftime("%H: %M: %S, %d-%m-%y")
print(now)

target_datetime = datetime.datetime(2020, 1, 1, 12, 30, 59)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")