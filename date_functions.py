from datetime import datetime, timedelta
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

def get_first_date_of_current_month():
    replace_date = datetime.today().replace(day=1)
    first_date = replace_date.strftime('%Y-%m-%d')
    return first_date
  
 def get_last_date_of_current_month():
    last_date = datetime.now() + timedelta(days=-1)
    last_date = last_date.strftime('%Y-%m-%d')
    return last_date

def get_first_date_of_last_month():
    d = datetime.today()
    month, year = (d.month-1, d.year) if d.month != 1 else (12, d.year-1)
    first_date = d.replace(day=1, month=month, year=year)
    return first_date
  
  def get_last_date_of_last_month():
    current_month = get_last_date_of_current_month()
    first_date = current_month.replace(day=1)
    last_date = first_date - timedelta(days=1)
    return last_date
  
  
one_year_ago = (datetime.now() + timedelta(days=-365)).strftime('%Y-%m-%d')
print(type(one_year_ago))
one_year_ago = (datetime.now() + timedelta(days=-365))
print(one_year_ago)


start_date = get_first_date_of_last_month()
end_date = get_last_date_of_last_month()
#end_date = one_year_ago
print(start_date, end_date)

if start_date < end_date:
    state = date_to_string(start_date)
    toDate = date_to_string(end_date)
    print(state, toDate)
else:
    state = date_to_string(get_first_date_of_last_month())
    toDate = date_to_string(get_last_date_of_last_month())
    print(state, toDate)
