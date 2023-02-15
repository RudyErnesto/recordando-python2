"""
    F   E   C   H   A   S
"""
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
now = datetime.now()
print(now)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023,1,1)
print_date(year_2023)

### tiem

current_time = time(22, 2, 7)
print(current_time.hour)
print(current_time.min)
print(current_time.second)


##date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date=date(2022, 11, 7)
print(current_date)

### operaciones con fechas

diff = year_2023 - now
print(diff)


## timedelta

start_timedelta = timedelta(200, 100, 90, weeks=10)
end_tiemedelta= timedelta(300, 100, 100, weeks= 13)
print(end_tiemedelta - start_timedelta)
print(end_tiemedelta + start_timedelta)