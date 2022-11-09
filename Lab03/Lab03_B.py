from datetime import datetime
from dateutil.relativedelta import relativedelta

def n_times_day(bday1, bday2, n=2):
    age_delta = bday2 - bday1
    n_times_day = bday2 + age_delta / (n-1)
    
    return n_times_day


def current_time_and_day():
    now = datetime.now()
    return now


def main():

    print("Lab03 B-1")
    print("Today's date and the day of the week:")
    print(current_time_and_day())
    print(current_time_and_day().strftime("%A"))

    # Your output should be like:
    # 2020-08-03 20:19:19.806211
    # Monday

    print("\nLab03 B-2")
    s = input('Enter your birthday in mm/dd/yyyy format: ') #'1/15/1997'
    print("Time until your next birthday and your current age are:")
    now = datetime.now()
    next_year = relativedelta(years=+1)
    format_s = "%m/%d/%Y"  # indicate the format of s for instantiating datetime using strptime

    BDAY = datetime.strptime(s,format_s)
    bday_this_year = BDAY.replace(year=now.year) 

    if datetime.now() < bday_this_year:  # if it hasn't pass your birthday this year
        next_bday = bday_this_year  
    else:
        next_bday = bday_this_year + next_year

    print(next_bday - now)
    print(relativedelta(now, BDAY).years)

    # Your output should be like:
    # 280 days, 3:40:40.193789
    # 22

    print("\nLab03 B-3")
    print("For people born on these dates:")
    bday1 = datetime(day=15, month=1, year=1997)
    bday2 = datetime(day=11, month=10, year=2003)
    print("Double Day is")
    print(bday2 + (bday2 - bday1))

    # Your output should be like:
    # 2020-01-01 00:00:00 (this is not the correct answer!)

    print("\nLab03 B-4")
    print("Triple Day is ")
    print(n_times_day(bday1, bday2, n=3))


if __name__ == '__main__':
    main()