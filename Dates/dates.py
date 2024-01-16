from datetime import datetime,timezone,timedelta, date
from dateutil import relativedelta

print(datetime.now())
print(datetime.now() - timedelta(days=2, hours=2))
print(datetime.now() - relativedelta.relativedelta(months=2))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(datetime(2019,1,25,11,22,54))
print(datetime.today())
print(datetime.astimezone(datetime.now(),tz=timezone.utc))
print(date.today())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().hour)
print(datetime.now().year)