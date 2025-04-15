import datetime
date = datetime.date(2025,1,1)
today= datetime.date.today()

print(date)
print(today)

time = datetime.time(12,30,0)
today_time= datetime.datetime.now()

today_time = today_time.strftime("%H:%M:%S  %d-%m-%Y")

print(time)
print(today_time)




