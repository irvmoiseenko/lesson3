from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta, MO

print(datetime.today().strftime('%A %d %B %Y'))

delta = timedelta(days=1)
a = datetime.today() - delta
print(a.strftime('%A %d %B %Y'))

date_month = date.today() + relativedelta(months=-1)
print(date_month.strftime('%A %d %B %Y'))



