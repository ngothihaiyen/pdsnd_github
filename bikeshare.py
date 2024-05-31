import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Input for city
    city = input('Which city\'s data would you prefer to analyze: Chicago, New York City, or Washington?\n').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        city = input('Please enter a valid city name (Chicago, New York City, or Washington).\n').lower()
    print('The city you choose is', city.title())

    # Input for month
    month = input('Which month\'s data would you prefer to analyze: choose from January to June or "all".\n').lower()
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        month = input('Please enter a valid month from January to June or "all".\n').lower()
    print('The month you choose is', month)

    # Input for day
    day = input('Which day\'s data would you prefer to analyze: choose a day of the week or "all".\n').lower()
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        day = input('Please enter a valid day of the week or "all".\n').lower()
    print('The day you choose is', day)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data into a df
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the 'Start Time', 'End Time' column to datetime and extract month and day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Month'] = df['Start Time'].dt.strftime('%B')
    df['Day of Week'] = df['Start Time'].dt.strftime('%A')
    
    # Filter by month if applicable
    if month != 'all':
        
        # Create a dictionary mapping month names to their corresponding numeric values
        month_mapping = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
                                               
        # Convert month name to numeric value using the mapping
        month_index = month_mapping.get(month.lower())
        
        # Filter by month index
        if month_index is not None:
           df = df[df['Start Time'].dt.month == month_index]
        
    # Filter by day of week if applicable
    if day != 'all':
          
          # Convert day name to title case
          day_name = day.title()
          
          # Filter by day of week
          df = df[df['Day of Week'] == day_name]
    return df
            
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print('The mosth common month is', common_month)

    # TO DO: display the most common day of week
    common_day = df['Day of Week'].mode()[0]
    print('The most common day is', common_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Hour'].mode()[0]
    print('The most common start hour is', common_start_hour)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The mode common end station is', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('The most common trip is', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def convert_seconds(seconds):
    # Caculate the number of days
    days = seconds // (24 * 3600)
    
    # Caculate the remaining hours after removing days
    remaining_seconds = seconds % (24 * 3600)
    hours = remaining_seconds // 3600
    
    # Caculate the remaining minutes after removing hours
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    
    # Caculate the remaining seconds after removing minutes
    seconds = remaining_seconds % 60
    
    return days, hours, minutes, round (seconds, 1)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_days, total_hours, total_minutes, total_seconds = convert_seconds(total_travel_time)
    print(f'Total travel time is {total_days} days, {total_hours} hours, {total_minutes} minutes, {total_seconds: .1f} seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_days, mean_hours, mean_minutes, mean_seconds = convert_seconds(mean_travel_time)
    print(f'Mean travel time is {mean_days} days, {mean_hours} hours, {mean_minutes} minutes, {mean_seconds: .1f} seconds')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('\nCount of gender:')
        print(df['Gender'].value_counts())
    else: 
        print('\nGender data is not avaiable for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    # Display the earliest birth year
    if 'Birth Year' in df.columns:
        print('\nThe earliest birth year is', int(df['Birth Year'].min()))
    
    # Display the most recent birth year
        print('\nThe most recent birth year is',int(df['Birth Year'].max()))
        
    # Display the most common birth year
        print('\nThe most common birth year is', int(df['Birth Year'].mode()[0]))
    else:
        print('\nBirth year data is not avaiable for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Ask the user if they want to display the first 5 rows of data
    while True:
        display_data_first = input('Do you want to display the first 5 rows of data? Enter yes or no.\n').lower()
        if display_data_first == 'yes':
            print(df.head())
            break
        elif display_data_first == 'no':
            break
        else:
            print('Please enter "yes" or "no".')

    # Ask the user if they want to display the next 5 rows of data, repeatedly until they say no
    index = 5
    while True:
        display_data_next = input('Do you want to display the next 5 rows? Enter yes or no.\n').lower()
        if display_data_next == 'yes':
            print(df[index:index+5])  # Display the next 5 rows
            index += 5
        elif display_data_next == 'no':
            break
        else:
            print('Please enter "yes" or "no".')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return df
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
