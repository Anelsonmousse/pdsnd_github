import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

# Define mappings for months and days
month_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
day_map = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Which city would you like to analyze? (chicago, new york city, washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city. Please try again.')

    while True:
        month = input('Which month would you like to filter by? (all, january, february, ... , june): ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid month. Please try again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of the week would you like to filter by? (all, monday, tuesday, ... sunday): ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid day of the week. Please try again.')

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    # Convert the start_time column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month != 'all':
        df = df[df['Start Time'].dt.month == month_map[month]]

    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['Start Time'].dt.weekday == day_map[day]]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_counts = df['Start Time'].dt.month.value_counts().sort_values(ascending=False)
    most_common_month = month_map.get(month_counts.index[0])
    print('Most common month:', most_common_month)

    # TO DO: display the most common day of week
    day_of_week_counts = df['Start Time'].dt.weekday.value_counts().sort_values(ascending=False)
    most_common_day_of_week = day_map.get(day_of_week_counts.index[0])
    print('Most common day of week:', most_common_day_of_week)

    # TO DO: display the most common start hour
    start_hour_counts = df['Start Time'].dt.hour.value_counts().sort_values(ascending=False)
    most_common_start_hour = start_hour_counts.index[0]
    print('Most common start hour:', most_common_start_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_counts = df['Start Station'].value_counts().sort_values(ascending=False)
    most_commonly_used_start_station = start_station_counts.index[0]
    print('Most commonly used start station:', most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    end_station_counts = df['End Station'].value_counts().sort_values(ascending=False)
    most_commonly_used_end_station = end_station_counts.index[0]
    print('Most commonly used end station:', most_commonly_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station_counts = df[['Start Station', 'End Station']].value_counts().sort_values(ascending=False)
    most_frequent_start_end_station_trip = start_end_station_counts.index[0]
    print('Most frequent combination of start station and end station trip:', most_frequent_start_end_station_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_type_counts)

    # Check if 'Gender' column exists in the DataFrame
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts().sort_values(ascending=False)
        print('Counts of gender:')
        print(gender_counts)
    else:
        print('Gender data not available for this city.')

    # Check if 'Birth Year' column exists in the DataFrame
    if 'Birth Year' in df.columns:
        birth_year_counts = df['Birth Year'].value_counts().sort_values(ascending=False)
        most_common_birth_year = birth_year_counts.index[0]
        print('Earliest year of birth:', df['Birth Year'].min())
        print('Most recent year of birth:', df['Birth Year'].max())
        print('Most common year of birth:', most_common_birth_year)
    else:
        print('Birth Year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw data to the user."""
    start_row = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no: ')
        if view_data.lower() != 'yes':
            break
        print(df.iloc[start_row:start_row+5])
        start_row += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
