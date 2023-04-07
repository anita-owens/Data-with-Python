from datetime import date, datetime, timedelta
from calendar import monthrange

def date_to_string(date):
    '''
    Needs to match preferred string-format
    
    Parameters
    ----------
    date : datetime.datetime object
        date to be converted to string

    Returns
    -------
    string:
        string version of date

    '''
    return date.strftime("%Y-%m-%d")
print(date_to_string.__doc__)

# CURRENT MONTH --------------------------------
def get_first_date_of_current_month():
    '''Returns the first day of this month YYYY-MM-DD as a string.'''
    replace_date = datetime.today().replace(day=1)
    first_date = replace_date.strftime('%Y-%m-%d')
    return first_date
get_first_date_of_current_month()
print(get_first_date_of_current_month.__doc__)


def get_first_date_of_current_month():
    return date.today().replace(day=1).strftime('%Y-%m-%d')
get_first_date_of_current_month()

##Simplified version
def get_first_date_of_current_month():
    return date.today().replace(day=1)
get_first_date_of_current_month()

  
def get_last_date_of_current_month():
    '''Returns the last day of this month YYYY-MM-DD as a datetime object. We are going to use this function in another function'''
    date_value = datetime.today() + timedelta(days=-1)
    last_date = date_value.replace(day = monthrange(date_value.year, date_value.month)[1])
    return last_date
get_last_date_of_current_month()
date_to_string(get_last_date_of_current_month()) # Convert to a string

#1 Eliminates use of the calendar package
def get_last_date_of_current_month():
    '''Returns the last day of this month YYYY-MM-DD as a datetime object'''
    today = datetime.today()
    last_day_of_this_month = datetime(today.year, today.month, 1) + timedelta(days=32)
    return last_day_of_this_month.replace(day=1) - timedelta(days=1)
get_last_date_of_current_month()
date_to_string(get_last_date_of_current_month())

# PRIOR MONTH --------------------------------
def get_first_date_of_last_month():
    '''Returns the first day of the prior month'''
    d = datetime.today()
    month, year = (d.month-1, d.year) if d.month != 1 else (12, d.year-1)
    first_date = d.replace(day=1, month=month, year=year)
    return first_date
date_to_string(get_first_date_of_last_month())

#2
from dateutil.relativedelta import relativedelta
def get_first_date_of_last_month():
    '''Returns the first day of the prior month YYYY-MM-DD.'''
    return (datetime.date.today() - relativedelta(months=1)).replace(day=1).strftime('%Y-%m-%d')

# Return object is a datetime object
from dateutil.relativedelta import relativedelta
def get_first_date_of_last_month():
    '''Returns the first day of the prior month YYYY-MM-DD.'''
    return (datetime.date.today() - relativedelta(months=1)).replace(day=1)
get_first_date_of_last_month()


def get_last_date_of_last_month():
    '''Returns the last day of the prior month YYYY-MM-DD.'''
    current_month = get_last_date_of_current_month()
    first_day_of_last_month = current_month.replace(day=1)
    last_day_of_last_month = first_day_of_last_month - timedelta(days=1)
    return last_day_of_last_month
get_last_date_of_last_month()
date_to_string(get_last_date_of_last_month())
  
#3
def get_last_date_of_last_month():
    '''Returns the last day of the prior month YYYY-MM-DD.'''
    today = datetime.today()
    first_day_of_month = datetime(today.year, today.month, 1)
    last_day_of_last_month = first_day_of_month - timedelta(days=2)
    return last_day_of_last_month
get_last_date_of_last_month()

one_year_ago = (datetime.now() + timedelta(days=-365)).strftime('%Y-%m-%d')
print(type(one_year_ago))
one_year_ago = (datetime.now() + timedelta(days=-365))
print(one_year_ago)

start_date = get_first_date_of_last_month()
end_date = get_last_date_of_last_month()
print(start_date, end_date)

##FiveTran
#Testing that end dates comes after the start date
if start_date < end_date:
    state = date_to_string(start_date)
    toDate = date_to_string(end_date)
    print(state, toDate)
#If not, then we will take the first day of the prior month as the start date and the last day of the prior month as the end date
else:
    state = date_to_string(get_first_date_of_last_month())
    toDate = date_to_string(get_last_date_of_last_month())
    print(state, toDate)

# As a function
def get_start_and_end_dates():
    if start_date < end_date:
        state = date_to_string(start_date)
        toDate = date_to_string(end_date)
        return state, toDate
    else:
        state = date_to_string(get_first_date_of_last_month())
        toDate = date_to_string(get_last_date_of_last_month())
        return state, toDate
state, toDate = get_start_and_end_dates()
print(state, toDate)