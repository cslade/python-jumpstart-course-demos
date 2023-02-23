import datetime



def header():
    print("-------------------------")
    print("Program 03 Birthday")
    print("-------------------------", end:="\n")


def get_user_birthday():
    year = int(input("What year were you born? [YYYY]: "))
    month = int(input("What month were you born? [MM]: "))
    day = int(input("What day were you born? [DD]: "))
    
    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_birthday(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    
    dt = this_year - target_date
    return dt.days
   

def print_birthday_info(days):
    if days < 0:
        print(f"You had a birthday {-days} days ago!")
    elif days > 0:
        print(f" You birthday wil be in {days} days!")   
    else:
        print("Happy birthday dude!")
    
    

def main():
    header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_birthday(bday, today)
    print_birthday_info(number_of_days)
    
    
main()

