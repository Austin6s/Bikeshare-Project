import time
import pandas as pd
import sys

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
||||||| parent of e19af20 (Just slightly changed some alignment)

=======
>>>>>>> e19af20 (Just slightly changed some alignment)
#Adding this comment to have something to pull
||||||| parent of 20ddfd3 (Added a comment at the top)
=======
#Pushed this project to a remote git repository on Github
<<<<<<< HEAD
>>>>>>> 20ddfd3 (Added a comment at the top)
||||||| parent of e19af20 (Just slightly changed some alignment)
=======

>>>>>>> e19af20 (Just slightly changed some alignment)
||||||| parent of 3e1e194 (Added another comment for fun)
=======
#I need to make a change to this code but idk what to change since it's already awesome and I don't want to break it haha
>>>>>>> 3e1e194 (Added another comment for fun)
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',
              'nyc': 'new_york_city.csv',
              'ny': 'new_york_city.csv',
              'new york': 'new_york_city.csv',
              'dc': 'washington.csv'}

def input_prompt(message, valid_input_list):
    '''This function is to handle user inputs that may be invalid and provides a simple workflow to walk through a process for whatever the user inputs

    INPUT:
    message: str. The initial message requesting the user input.
    valid_input_list: list. The list containing all of the acceptable inputs from the user.

    OUTPUT: A valid user input.'''

    while True:
            initial_input = input(message + '\n').lower()
            print()
            if initial_input in valid_input_list:
                print('Thanks for the entry! Please wait a moment while we query your data...\n')
                break
            #in case someone wants to exit the loop without closing the program or terminal
            elif initial_input == 'exit':
                sys.exit('Have a great day!')
            else:
                print('''Oops looks like you didn\'t enter a valid input, please try again :)
Or if you would like to terminate this program just type: \'exit\'\n''')
    return initial_input

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    #first I want to set month and day variable to null values to avoid any UnboundLocalErrors if the user chooses to look at only one of those variables
    month = None
    day = None

    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_prompt('Which city would you like to see data from? (Chicago, New York, or Washington)', CITY_DATA)

    #filter by month or day or all (both)
    fltr = input_prompt('Select your filter: month, day, none. (For example, if you select \'month,\' no day data will be displayed and vice versa. If you select, \'none,\' then you will have access to both', ['month', 'day', 'none'])

    #define acceptable inputs for both the month and day variables
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    #get user input for months
    if fltr in ['month', 'none']:
        month = input_prompt('Which month? (for all months type \'all\')', months)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if fltr in ['day', 'none']:
        day = input_prompt('Which day of the week? (for all days of the week type \'all\')', days)
    print('-'*40)

    return city, month, day

def display_data(df):
    '''Upon request, displays data 5 rows at a time'''

    response = input_prompt('Before we show some random stats we thought were cool, would you like to dig into this juicy dataset a bit yourself? If you would like to view 5 rows of individual trip data, enter \'yes\'. Otherwise enter \'no\' to move on with your life.', ['yes', 'no', 'y', 'n', 'sure', 'nah'])
    start_loc = 0
    while response in ['yes', 'y', 'sure']:
        pd.set_option('display.max_columns', None)
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        response = input_prompt('Hey there dataphile! Want to see 5 more rows of this super duper cool dataset?', ['yes', 'no', 'y', 'n', 'nah', 'sure'])
    print('-'*40)
    print('Okay chill for a second while we show you the stats we feel like showing you, but don\'t worry you don\'t have to wait long because this code was written super efficiently ;)')

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month not in [None, 'all']:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day not in [None, 'all']:
        # use the index of the days list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    pop_month = df['month'].mode()[0]
    print('Most popular month for traveling: ')
    print(months[pop_month - 1].title())

    # display the most common day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    pop_day = df['day_of_week'].mode()[0]
    print('Most popular day of the week: ')
    print(days[pop_day].title())

    # display the most common start hour
    pop_hour = df['hour'].mode()[0]
    print('Most popular hour: ')
    print('{}:00'.format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start = df['Start Station'].mode()[0]
    print('Most popular start station is:')
    print(pop_start)
    # display most commonly used end station
    pop_end = df['End Station'].mode()[0]
    print('Most popular end station is:')
    print(pop_end)

    # display most frequent combination of start station and end station trip
    pop_combo = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most popular trip start and end stations:')
    print(pop_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttl_time = df['Trip Duration'].sum()
    print('The total travel time of all users was: ')
    print('{} hours, {} minutes, and {} seconds'.format(int(ttl_time/3600), int(ttl_time%3600/60), ttl_time%3600%60))
    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Displaying number of users broken down by type:')
    print(user_types)
    print()
    # Display counts of gender
    if 'Gender' in df.columns:
        g_count = df['Gender'].value_counts()
        print('Displaying number of users broken down by gender:')
        print(g_count)
        print()
    else:
        print('***No gender data in this data set***')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_by = df['Birth Year'].min()
        print('The birth year of the oldest user(s) was:')
        print(earliest_by)
        print()
        latest_by = df['Birth Year'].max()
        print('The birth year of the youngest user(s) was:')
        print(latest_by)
        print()
        mst_common_by = df['Birth Year'].mode()[0]
        print('The most common birth year for users was:')
        print(mst_common_by)
    else:
        print('***No birth year data in this data set***')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input_prompt('If you would like to restart, type \'yes.\' Otherwise type \'exit\' to terminate this program.', ['y', 'yes', 'yes.', 'sure'])
        if restart not in ['yes', 'y', 'yes.', 'sure']:
            break


if __name__ == "__main__":
	main()
