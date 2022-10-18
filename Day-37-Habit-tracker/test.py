import datetime as dt

# now = dt.datetime.now()
# now_1 = str(now.date_raw())
# date_raw = now_1.replace('-', '')
# print(date_raw)

date_raw = dt.datetime.now().date()
date = date_raw.strftime("%Y%m%d")

print(date)

yesterday_raw = dt.datetime(year=date_raw.year, month=date_raw.month, day=date_raw.day - 1)
model_date = yesterday_raw.strftime("%Y%m%d")

print(model_date)