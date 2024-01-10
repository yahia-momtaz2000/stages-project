import calendar
from datetime import datetime
from dateutil import relativedelta

# print(dir(datetime)) # show all methods in this class

print(datetime.now()) # print current date and time

print(datetime.now().date()) # print current date only
print(datetime.now().date().year)
print(datetime.now().date().month)
print(datetime.now().date().day)
print(datetime.now().date().weekday()) # Mon = 0

print(datetime.now().time()) # print current time only
print(datetime.now().time().hour)
print(datetime.now().time().minute)
print(datetime.now().time().second)


print('------- # formatting date : Convert from Date to String to show in a custom format ---------')
today_date = datetime.now()
# formatting date : Convert from Date to String
print(today_date.strftime('%d-%m-%y-%Y-%w'))
print(today_date.strftime('%B-%b-%A-%a'))
print(today_date.strftime('%H-%M-%S')) # time in 24 hours
print(today_date.strftime('%I-%M-%S %p')) # time in 12 hours

print('---- custom date : 12 - May - 2021 : Create date objects with 2 ways ---')
print('-- 1. from datetime class as object')
custom_date = datetime(2021, 5, 12)
print(custom_date)
# Convert from String again to Date
print('---- 2.# from Convert from String to Date ---------')
custom_date = '24-05-2021' # String value
print(type(custom_date))
custom_date = datetime.strptime(custom_date,'%d-%m-%Y') # now converted to date value
print(custom_date)
print(type(custom_date))
print( datetime.strftime(custom_date, '%d %B %Y') )
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++

print('-------- Dates Comparison ------------')
# Dates Comparison
if today_date > custom_date:
    print('today is greater than custom date')
elif today_date < custom_date:
    print('today is less than custom date')
else:
    print('today is equal to custom date')

print('----- # Months between 2 dates : using relativedelta class from dateutil module ---')
# Months between 2 dates : using relativedelta class from dateutil module
differ = relativedelta.relativedelta(today_date, custom_date)
print('----> from date', today_date,' ||| custom date | ', custom_date)
print(differ.years, 'Years,', differ.months, 'months,', differ.days, 'days',
      differ.hours, 'Hours ', differ.minutes, 'Minutes', differ.seconds, 'seconds')

# Differ in Days Totally :
print('-----  Differ in Days Totally  -----')
date1 = datetime(2023, 12, 15)
date2 = datetime(2023, 10, 20)
difference_days = (date1 - date2).days
print(type(difference_days))
print(f'Different days = {difference_days}')


# Adding Or Subtract 1 year and 6 Months and 5 days to today Date
print('---------- Adding Or Subtract 1 year and 6 Months and 4 days to today Date  ----------')
print(f'today date = {today_date}')
new_date = today_date + relativedelta.relativedelta(years=1, months=6, days= 4)
print(new_date)
print(type(new_date))
print('---- The First, Last day of current month ----')
# The Last day of current month
first_day = today_date + relativedelta.relativedelta(day=1)
last_day = today_date + relativedelta.relativedelta(day=31)
print('first day = ', first_day)
print('last day = ', last_day)

# --- find the next sunday date from today----
print('---- find the next sunday date from today----')
next_sunday = today_date + relativedelta.relativedelta( weekday=calendar.SUNDAY)
print(f'Next sunday = {next_sunday}')

# --- find the 2nd next sunday date from today----
print('---- find the 2nd next sunday date from today----')
next2nd_sunday = today_date + relativedelta.relativedelta(weekday=calendar.SUNDAY, weeks= 1)
print(f'Next sunday = {next2nd_sunday}')

# --- find the 1st sunday from the beginning of the next month ----
print('---- find the 1st sunday from the beginning of the next month ----')
next_month_sunday = today_date + relativedelta.relativedelta(weekday=calendar.SUNDAY, months=1, day= 1)
print(f'Next sunday = {next_month_sunday}')


# --- find the 1st sunday from the beginning of the current month ----
print('--- find the 1st sunday from the beginning of the current month ----')
current_month_sunday = today_date + relativedelta.relativedelta(weekday=calendar.SUNDAY, day=1)
print(current_month_sunday)



# --- find the 1st sunday from the beginning of the next year ----
print('--- find the 1st sunday from the beginning of the next year ----')
next_year_sun = today_date + relativedelta.relativedelta(weekday=calendar.SUNDAY, years=1, month=1, day=1)
print(next_year_sun)


# --- find the 1st sunday from the beginning of the current year ----
print('--- find the 1st sunday from the beginning of the current year ----')
current_year_sun = today_date + relativedelta.relativedelta(weekday=calendar.SUNDAY, month=1, day=1)
print(current_year_sun)

# ------ write a program to round a date to the nearest month start
print('---- write a program to round a date to the nearest month start ----')
input_date = datetime(2023, 7, 14)  # Date to round
if input_date.day >= 15:
    rounded_date = input_date + relativedelta.relativedelta(months = 1, day = 1)
else:
    rounded_date = input_date + relativedelta.relativedelta(day = 1)

print(f'Rounded date to the nearest month start = {rounded_date}')

# ----------- Write a program to count weekday Fri in a specific month
print('----------- Write a program to count weekday Fri in a specific month')
year = 2023
month = 6
input_date = datetime(year, month, 1)
month_last_day = input_date + relativedelta.relativedelta(input_date, days = 31)
count_weekends = 0
while input_date.month == month:
    count_weekends += 1
    input_date = input_date + relativedelta.relativedelta(weekday = calendar.FRIDAY , weeks=1)

print(f'Count of weekend days = {count_weekends}')

# ----------- Write a program to count weekdays Fri or Sat. in a specific month
print('----------- Write a program to count weekday Fri or Sat. in a specific month')
year = 2023
month = 6
input_date = datetime(year, month, 1)
month_last_day = input_date + relativedelta.relativedelta(input_date, days = 31)
count_weekends = 0
while input_date.month == month:
    if input_date == input_date + relativedelta.relativedelta(weekday = calendar.FRIDAY)\
           or  input_date == input_date + relativedelta.relativedelta(weekday = calendar.SATURDAY):
        count_weekends += 1
    # if input_date.weekday() in [4, 5]: Another solution  | Monday = 0

    input_date = input_date + relativedelta.relativedelta(days=1)
print(f'Count of weekend days = {count_weekends}')

# ----------- Write a program to GEt the date after 12 Working days from a date
print('----------- Write a program to GEt the date after 12 Working days from a date ')
input_date = datetime(2023, 12, 22)  # start date
# if start date is Friday; jump 1 day
if input_date == input_date + relativedelta.relativedelta(weekday= calendar.FRIDAY):
    input_date = input_date + relativedelta.relativedelta(days = 1)
copy_start_date = input_date
jump_days = 12
for i in range(12):
    if input_date == input_date + relativedelta.relativedelta(weekday = calendar.THURSDAY):
        input_date = input_date + relativedelta.relativedelta(days = 3)
    else:
        input_date = input_date + relativedelta.relativedelta(days = 1)
print(f'After {jump_days} days from {copy_start_date.date()} date, this will be {input_date.date()} date')

# ---------- Find the earliest date from a list of dates ------
print('---------- Find the earliest date from a list of dates ------')
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
print(f'The Min date in the list is {min(dates_list)}')
min_date = dates_list[0]
for date in dates_list:
    if date < min_date:
        min_date = date
print(f'The Min date in the list is {min_date}')

# ------ Check if a specific date exists in a tuple of dates ----
print('---- Check if a specific date exists in a List of dates -----')
given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]
for my_date in dates_list:
    if given_date == my_date:
        print(f'{given_date} is found in the list at index {dates_list.index(my_date)}')
        break
else:
        print(f'{given_date} is not found in this list')


# ---- program checks if a specific date falls between two provided dates.
print('--- ---- program checks if a specific date falls between two provided dates. -----')
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

if start_date <= given_date <= end_date:
    print('The date is in range')
else:
    print('The date is not in range')


# --- program checks which date falls within the range of date tuples provided in a list. ----
print('--- program checks which date falls within the range of date tuples provided in a list. ----')
dates_list = [
    (datetime(2023, 1, 1), datetime(2023, 1, 10)),
    (datetime(2023, 1, 15), datetime(2023, 1, 20)),
    (datetime(2023, 2, 5), datetime(2023, 2, 15))
]
given_date = datetime(2023, 1, 24)

for my_date in dates_list:
        if my_date[0] <= given_date <= my_date[1]:
            print(f'The date {given_date.date()} is within the range of {my_date[0].date() } and {my_date[1].date()}')
            break
else:
    print(f'The date {given_date.date()} is NOT within the range')
