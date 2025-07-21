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

#More efficient version
import datetime
def get_first_date_of_last_month():
    '''Returns the first day of the prior month'''
    today = datetime.date.today()
    first_date_of_this_month = today.replace(day=1)
    last_month = first_date_of_this_month - datetime.timedelta(days=1)
    first_date_of_last_month = last_month.replace(day=1)
    return first_date_of_last_month
date_to_string(get_first_date_of_last_month())


#2
from dateutil.relativedelta import relativedelta
def get_first_date_of_last_month():
    '''Returns the first day of the prior month YYYY-MM-DD.'''
    return (datetime.date.today() - relativedelta(months=1)).replace(day=1).strftime('%Y-%m-%d')

# Return object is a datetime object not a string
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
    today = datetime.date.today()
    first_day_of_month = datetime(today.year, today.month, 1)
    last_day_of_last_month = first_day_of_month - timedelta(days=1)
    return last_day_of_last_month
get_last_date_of_last_month()



#Apparently using today is more efficient
def get_last_date_of_last_month():
    '''Returns the last day of the prior month YYYY-MM-DD.'''
    today = datetime.date.today()
    first_day_of_month = today.replace(day=1)
    last_day_of_last_month = first_day_of_month - timedelta(days=1)
    return last_day_of_last_month
date_to_string(get_last_date_of_last_month())


one_year_ago = (datetime.now() + timedelta(days=-365)).strftime('%Y-%m-%d')
print(type(one_year_ago))
one_year_ago = (datetime.now() + timedelta(days=-365))
print(one_year_ago)

start_date = get_first_date_of_last_month()
end_date = get_last_date_of_last_month()
print(start_date, end_date)


today = datetime.today()
print(today)

today_string = datetime.today()
print(date_to_string(today_string))


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

##FiveTran
request = "request"
# As a function
def get_start_and_end_dates():
    if not request["state"]:
        fromDate = date_to_string((datetime.today() + timedelta(days=-365)))
        toDate = date_to_string(get_last_date_of_last_month())
        return fromDate, toDate
    else:
        fromDate = date_to_string(get_first_date_of_last_month())
        toDate = date_to_string(get_last_date_of_last_month())
        return fromDate, toDate
fromDate, toDate = get_start_and_end_dates()
print(fromDate, toDate)
#state = toDate
state = data[-1]['id']



def get_state():
    if not request["state"]:
        state = '2022-09-01'
    else:
        state = request["state"]["date"]
        return state

if not request["state"]:
    state = '2022-09-01'
else:
    state = request["state"]["date"]

# Python3 code to demonstrate working of
# Get Last date of Month
# Using replace() + timedelta()
import datetime

# initializing date
test_date = datetime.datetime(2023, 4, 10)
			
# printing original date
print("The original date is : " + str(test_date))

# getting next month
# using replace to get to last day + offset
# to reach next month
nxt_mnth = test_date.replace(day=28) + datetime.timedelta(days=4)

# subtracting the days from next month date to
# get last date of current Month
res = nxt_mnth - datetime.timedelta(days=nxt_mnth.day)

# printing result
print("Last date of month : " + str(res.day))




def get_last_date_of_last_month():
    '''Returns the last day of the prior month YYYY-MM-DD.'''
    today = datetime.now()
    first_day_of_month = datetime(today.year, today.month, 1)
    last_day_of_last_month = first_day_of_month - timedelta(days=1)
    return last_day_of_last_month
get_last_date_of_last_month()


def get_last_date_of_last_month():
    '''Returns the last day of the prior month YYYY-MM-DD.'''
    today = datetime(2023, 5, 1)
    first_day_of_month = datetime(today.year, today.month, 1)
    last_day_of_last_month = first_day_of_month - timedelta(days=1)
    return last_day_of_last_month
get_last_date_of_last_month()


## Code Changes
def get_first_date_of_last_month():
    '''Returns the first day of the prior month'''
    today = datetime.date.today()
    first_date_of_this_month = today.replace(day=1)
    last_date_of_last_month = first_date_of_this_month - timedelta(days=1)
    first_date_of_last_month = last_date_of_last_month.replace(day=1)
    return first_date_of_last_month
date_to_string(get_first_date_of_last_month())


def get_first_date_of_last_month():
    '''Returns the first day of the prior month'''
    today = datetime.date.today()
    first_date_of_this_month = today.replace(day=1)
    last_date_of_last_month = first_date_of_this_month - timedelta(days=1)
    first_date_of_last_month = last_date_of_last_month.replace(day=1)
    return first_date_of_last_month
date_to_string(get_first_date_of_last_month())


def get_last_date_of_last_month():
    '''Returns the last day of the prior month'''
    today = datetime.date.today()
    first_date_of_this_month = today.replace(day=1)
    last_date_of_last_month = first_date_of_this_month - timedelta(days=1)
    return last_date_of_last_month
date_to_string(get_last_date_of_last_month())

# To test in Cloud function
secrets = {
	"secrets": {
		"client_id": "rdtjBtOkzZQE7_XzbAcBmQ",
		"api_key": "QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx"
	},
	"state": {'2023-04-12'}
}


secrets["secrets"]
secrets['state']
print(secrets.keys())
#Safely getting one value base don key
print(secrets.get('state'))

#Type is a dict
type(secrets['state'])

#state = business_table[-1]['id']

secrets2 = {"state": '01/01/21'}
secrets2
secrets2["state"]

##Scenario 1
#Value returned is 2023-04-01
request = {
	"secrets": {
		"client_id": "rdtjBtOkzZQE7_XzbAcBmQ",
		"api_key": "QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx"
	},
	"state": '2023-04-01'
}
if not request["state"]:
    state = '2022-09-01'
else:
    state = request["state"]
print(state)

#Scenario 2 Empty State - returns 2022-09-01
request = {
	"secrets": {
		"client_id": "rdtjBtOkzZQE7_XzbAcBmQ",
		"api_key": "QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx"
	},
	"state": {}
}
if not request["state"]:
    state = '2022-09-01'
else:
    state = request["state"]
print(state)


#Scenario 3 - Returns the string object in prior state 2023-04-01
request = {
	"secrets": {
		"client_id": "rdtjBtOkzZQE7_XzbAcBmQ",
		"api_key": "QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx"
	},
	"state": '2023-04-01'
}
if not request["state"]:
    state = '2022-09-01'
else:
    state = request["state"]
print(state)

#Scenario 4 - State is a dict with a key-value pair. Returns the string object in prior state 2023-04-01
request = {
	"secrets": {
		"client_id": "rdtjBtOkzZQE7_XzbAcBmQ",
		"api_key": "QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx"
	},
	"state": {'sample_table':'2023-04-01'}
}
if not request["state"]:
    state = '2022-09-01'
else:
    state = request["state"]["sample_table"]
print(state)


from datetime import datetime as dt
timestamp = dt.now().strftime("%Y-%m-%d %H:%M:%S")
today = dt.today().strftime("%Y-%m-%d %H:%M:%S.%f")
today_date = dt.today().strftime("%Y-%m-%d")
print(timestamp, today, today_date)

timestamp = dt.now()
today = dt.today()
print(timestamp, today)
