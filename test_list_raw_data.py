import argparse
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def process_args():
    """
    Accepts city, month and day input from the command line.

    Args:
        None
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    parser = argparse.ArgumentParser(description='Enter a city name, month and day of the week to be shown some interesting bikeshare statistics.')
    parser.add_argument('-c', '--city', required=True, help="Enter a city name: 'Chicago', 'New York City' or 'Washington'. Note that New York City should be surrounded in quotation marks.")
    parser.add_argument('-m', '--month', default='all', help="Enter a month: 'January', 'February', ... , 'June', default = 'All'")
    parser.add_argument('-d', '--day', default='all', help="Enter a day of the week: 'Monday', 'Tuesday', ... , 'Sunday', default = 'All'")
    args = parser.parse_args()

    city = args.city.lower()
    month = ('all' if (args.month == "") else args.month.lower())
    day = ('all' if (args.day == "") else args.day.lower())

    if city not in CITY_DATA:
        print('Error: {} is not one of \'Chicago\', \'New York City\', \'Washington\'!'.format(city.title())) 
        print('Exiting...')
        exit()

    if (month not in ('january', 'february', 'march', 'april', 'may', 'june') and month != 'all'):
        print('Invalid input! {} is either not a valid month or not included in the statistics.'.format(month.title()))
        exit()
    
    if (day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') and day != 'all'):
        print('Invalid input! {} is not a valid day.'.format(day.title()))
        exit()

    return city, month, day


def load_data(city, month, day): 
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError as e:
        print('File not found!\n{}'.format(e))
        exit()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1  
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def list_raw_data(df):

    """Displays a listing of the raw data 5 rows at a time until the end of the dataframe."""

    print('\nListing raw data...\n')
    start_time = time.time()

    # set counters and establish dataframe length
    next_ctr = 5
    prev_ctr = 0
    df_len = len(df) - 1

    ## check what happens at the end of the dataframe without prompting user
    while next_ctr <= df_len:
        print('\n{}'.format(df[prev_ctr:next_ctr]))
        prev_ctr = next_ctr
        next_ctr += 5

    # display the remainder of the dataframe... should be less than 5 rows
    if prev_ctr < df_len and next_ctr > df_len:
        print('\n{}'.format(df[prev_ctr:df_len]))
    
    print('\nExiting...\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    city, month, day = process_args()

    print('\n\nFilter criteria... \nCity: {}, Month(s): {}, Day(s): {}\n'.format(city.title(), month.title(), day.title()))
    print('-'*40)
        
    df = load_data(city, month, day)

    list_raw_data(df)

            
if __name__ == "__main__":
    main()