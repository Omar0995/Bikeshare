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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = 0
    while city not in CITY_DATA:
        city = input("Type the name of the city you would like to explore or type exit to exit: ").lower()
        if city in CITY_DATA:
            print("You have chosen: {}!".format(city))
        elif city == "exit":
            print('Now terminating the process. Have a nice day!')
            exit()
        else:
            print("Unfortunatly '{}' is not a valid city! try again.".format(city))

    # get user input for month (all, january, february, ... , june)
    months = ['All', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'Augest', 'September', 'October', 'November', 'December']
    month = input("Now Select a month to see it's data! or type 'all' to apply no filter: ").title()
    while month not in months:
        month = input('The month you entered is not valid! Please enter a valid month: ').title()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = input("Select a day of the week to filter by or type 'all' to continue without filteration: ").title()
    while day not in days:
        day = input('The day you entered is not valid! please enter a valid day: ').title()

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
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour
    df['Start to End Station'] = df['Start Station'] + ' ' + df['End Station']

    if month != 'All':
        df = df[df['Month'] == month]

    if day != 'All':
        df = df[df['Day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The month with the highest usage is: {}!'.format(df['Month'].mode()[0]))

    # display the most common day of week
    print('The day with the highest usage is: {}!'.format(df['Day'].mode()[0]))

    # display the most common start hour
    print('The most common starting hour is: {}!'.format(df['Start Hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: {}!'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is: {}'.format(df['Start to End Station'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total travel time for the selected period is about: {} hours!'.format(round((df['Trip Duration'].sum())/3600, 0)))

    # display mean travel time
    print('The mean travel time for the selected period is about: {} minutes!'.format(round(df['Trip Duration'].mean(), 0)/ 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Following is the data for user type: \n {}'.format(df['User Type'].value_counts()))

    if city != 'washington':
        # Display counts of gender
        print('Following is the data for user gender: \n {}'.format(df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
        print('The youngest user who used the service was born in: {}'.format(int(df['Birth Year'].max())))
        print('The Oldest User who used the service was born in: {}'.format(int(df['Birth Year'].min())))
        print('The year with the most number of users born in is: {}'. format(int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Display raw data when requested"""
    row = 0
    while True:
        viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.").title()
        if viewData == "Yes":
            print(df.iloc[row: row+5])
            row += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
