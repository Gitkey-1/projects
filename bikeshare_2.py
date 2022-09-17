import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_list = ['chicago','new york city','washington']
month_list = ['january' ,'february' ,'march' , 'april' , 'may' ,'june' ,'all']
day_list =['all' , 'monday' ,'tuesday' ,'wednesday', 'thursday','friday' ,'saturday' ,'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ''
    while True:
        city = input('Enter the city you would like to analyze:\n')
        if city.lower() in city_list:
           city = city.lower()
           break
        else:
           print('\nInvalid value, please enter city name \"chicago", \"new york city" or \"washington". ')

    month = ''
    while True:
        month = input('Enter the month you would like to filter or enter \"all" to not filter:\n')          
        if month.lower() in month_list :
           month = month.lower()
           break
        else:
           print('\nInvalid value, please enter month or \"all" to filter.')      
        
    day = ''
    while True:
        day = input('Enter the day of week you would like to filter or enter \"all" to not filter:\n')
        if day.lower() in day_list:
            day = day.lower()
            break
        else:
           print('\nInvalid value, please enter day of week or \"all" to filter.')          
    
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
  
    df['month'] = df['Start Time'].dt.month
    
    print('the most common month is: {}'.format(month_list[df['month'].mode()[0]-1]))
    
    df['day of week'] = df['Start Time'].dt.dayofweek
    
    print('the most common day of week is: {}'.format(day_list[df['day of week'].mode()[0]]))
    
    df['hour'] = df['Start Time'].dt.hour
    
    print('the most common hour is: {}:00'.format(df['hour'].mode()[0]))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    print('the most common start station is: {}.'.format(df['Start Station'].mode()[0]))
    
    print('the most common end station is: {}.'.format(df['End Station'].mode()[0]))
    
    print('the most combination of start and end station trip is: {}.'.format(df['Start Station'].mode()[0]+ 'to' + df['End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    print('the total travel time is :{} '.format(df['Trip Duration'].sum()))
    
    print('the mean travle time is : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
   
    types_count = df['User Type'].value_counts()
    print('the counts of user types is :{}.\n'.format(types_count))
    
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print('the counts of gender is :{}.\n'.format(gender_count))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe.\n')
   
    if 'Birth Year' in df.columns:
        earliest_birthyear = df['Birth Year'].min()
        recent_birthyear = df['Birth Year'].max()
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('the earliest year of birth is: {} \nthe most recent year of birth is: {} \nthe most common year of birth is: {}.'.format(earliest_birthyear,recent_birthyear,most_common_birthyear))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    num = 0
    print(df.head(num))
    while True:
        display = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()
        if display =='yes':
           num += 5
           print(df.iloc[num-5:num, :])
        elif display =='no':
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        while True:
            display = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()
            if display != 'yes':
                break
            raw_data(df)
            break
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main().run()
