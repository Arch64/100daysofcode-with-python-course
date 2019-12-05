'''Pybytes 67 

from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return start_100days + timedelta(days=100)


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    return (pycon_date - pybites_founded).days



from datetime import datetime

THIS_YEAR = 2018


def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    return THIS_YEAR - datetime.strptime(date, '%d %b, %Y').year


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    return datetime.strptime(date, '%d/%m/%Y').strftime('%m/%d/%Y')


print(years_ago('8 Aug, 2015'))
print(convert_eu_to_us_date('11/03/2002'))



from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    return datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_logs = [convert_to_datetime(line) for line in loglines if SHUTDOWN_EVENT in line]
    return max(shutdown_logs) - min(shutdown_logs)
    '''