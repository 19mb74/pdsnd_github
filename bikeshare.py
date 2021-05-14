# import os
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print('\nMost common month: {}'.format(df['month'].value_counts().idxmax()))
    # print('Most common month: {}'.format(df['month'].mode(0)[0]))
    

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    print('\nMost common day of the week: {}'.format(df['day_of_week'].value_counts().idxmax()))
    # print('Most common day of the week: {}'.format(df['day_of_week'].mode(0)[0]))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nMost common starting hour: {}'.format(df['hour'].value_counts().idxmax()))
    # print('Most common starting hour: {}'.format(df['hour'].mode(0)[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used starting station: {}'.format(df['Start Station'].value_counts().idxmax()))
    print('\nStart station hits for given time period: {}'.format(df['Start Station'].value_counts()[0]))

    # TO DO: display most commonly used end station
    print('\nMost commonly used ending station: {}'.format(df['End Station'].value_counts().idxmax()))
    print('\nEnd station hits for given time period: {}'.format(df['End Station'].value_counts()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    
    # Create a new dataframe that consists of only the start station and the end station columns
    df2 = pd.DataFrame(df['Start Station'])
    df2 = df2.join(df['End Station'])
    
    # Group the dataframe by trips
    journeys = df2.groupby(['Start Station','End Station']) 
    
    journey_dict = {}
    for key, value in journeys:
        # Add the number of rows belonging to the key to the dictionary
        journey_dict[key] = len(value)
    
    # Calculate the highest value in the dictionary based on its values
    highest_number_of_trips = max(journey_dict.values())
    # Borrowed this next line of code from Lesson 4, Solutions 40, and the Alternative solution
    # The idea is to loop through the dictionary and return the key (the trip) whose value matches the highest_number_of_trips
    # This could of course be more than one key... see Washington, January, Monday, for example
    most_popular_trip = [key for key, value in journey_dict.items() if value == highest_number_of_trips]
    print("\nMost popular trip(s):\n{}".format(most_popular_trip))
    print("\nNumber of trips made: {}".format(highest_number_of_trips))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
      
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nUser type count:\n{}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    # Since Washington has no data concerning customers'/subscribers' gender,
    # ...we need to use try/except 
    try:
        print('\nGender count:\n{}'.format(df['Gender'].value_counts()))
    except Exception as e:
        print('\nGender statistics are unavailable for this city.\n{}'.format(e))
        
    # TO DO: Display earliest, most recent, and most common year of birth
    # Since Washington has no data concerning customers'/subscribers' year of birth,
    # ...we need to use try/except 
    try:
        print('\nMost common year of birth: {}'.format(int(df['Birth Year'].value_counts().idxmax())))
        print('\nEarliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('\nMost recent year of birth: {}'.format(int(df['Birth Year'].max())))
    except Exception:
        print('Year of birth statistics are unavailable for this city.\n{}'.format(Exception))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum(),2)
    print('\nTotal travel time in seconds: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_time = round(df['Trip Duration'].mean(),2)
    print('\nAverage travel time in seconds: {}.'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
       

def list_raw_data(df):
    
    """Displays a listing of the raw data 5 rows at a time as requested by the user."""

    print('\nListing raw data...\n')
    start_time = time.time()

    # prompt user to view raw data
    raw_data_request = input('\n\nWould you like to see some raw data from the dataframe? (Y,y | N,n) ')
    # set counters and establish dataframe length
    next_ctr = 5
    prev_ctr = 0
    df_len = len(df) - 1
    
    ## check what happens at the end of the dataframe without prompting user
    # while next_ctr <= df_len:
    #     print('\n{}'.format(df[prev_ctr:next_ctr]))
    #     prev_ctr = next_ctr
    #     next_ctr += 5

    while raw_data_request.lower() == 'y' and next_ctr <= df_len:
        print('\n{}'.format(df[prev_ctr:next_ctr]))
        prev_ctr = next_ctr
        next_ctr += 5
        raw_data_request = input('\n\nWould you like to see some more? (Y,y | N,n) ')
        if raw_data_request.lower() == 'n':
            break
    
    # display the remainder of the dataframe... should be less than 5 rows
    if prev_ctr < df_len and next_ctr > df_len:
        print('\n{}'.format(df[prev_ctr:df_len]))
    
    print('\nExiting...\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def main():
    # clearConsole()
    city, month, day = process_args()

    print('\n\nFilter criteria... \nCity: {}, Month(s): {}, Day(s): {}\n'.format(city.title(), month.title(), day.title()))
    print('-'*40)
        
    df = load_data(city, month, day)
        
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

    list_raw_data(df)

            
if __name__ == "__main__":
    main()