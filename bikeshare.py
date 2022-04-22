import pandas as pd
import numpy as np
import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['all','january','february','march','april','may','june']
days=["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print_pause('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    
    while True :
        city=input("please choose a city \n ( 1-chicago  2-new york city - 3-washington ) ").lower()
        if city in CITY_DATA:
            break
                        
        elif city not in CITY_DATA :
            print_pause("invalid input")
            city=input("please choose a city \n ( 1-chicago  2-new york city - 3-washington ) ").lower()
                
     
                
        
                
    # TO DO: get user input for month (all, january, february, ... , june)
  

    
    
    while True:
        
        
        month=input("please Enter a month that you want to choose \n ( 1-all 2-january 3-february 4-march 5-april 6-may 7-june )").lower()
        if month in months:
            break
        else:
            
            print_pause("invalid input")
            month=input("please Enter a month that you want to choose \n 1-all 2-january 3-february 4-march 5-april 6-may 7-june").lower()            
      
   


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
  
    
    
    
    while True:
        
        day=input("please Enter a number of day that you want to choose \n ( 1-all 2-monday 3-tuesday 4-wednesday 5-thursday 6-friday 7-saturday 8-sunday )").lower()
        if day not in days:  
            print_pause("invalid input")
            day=input("please Enter a number of day that you want to choose \n ( 1-all 2-monday 3-tuesday 4-wednesday 5-thursday 6-friday 7-saturday 8-sunday )").lower()          
        else:   
            break            

    
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
    df=pd.read_csv(CITY_DATA[city])    #loding data into a dataframe
    #Converting Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #Converting month and day and hour to a datetime and extracting them
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print_pause(f"The most common month is {common_month}")

    # TO DO: display the most common day of week
    common_day_of_week=df['day_of_week'].mode()[0]
    print_pause(f"The most common day of week is {common_day_of_week}")

    # TO DO: display the most common start hour
    common_hour=df['hour'].mode()[0]
    print_pause(f"The most common hour is {common_hour}") 

    print_pause("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print_pause(f"The most common start station is : {common_start_station}") 

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print_pause(f"The most common end station is : {common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    combination=df['Start Station']+','+df['End Station']
    most_frequent_combination=combination.mode()[0]
    print_pause(f"The most frequent combination of start station and end station trip is : \n {most_frequent_combination} .")

    print_pause("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum().round()
    print_pause(f"Total travel time is {total_travel_time}")
    # TO DO: display mean travel time
    averag_travel_time=df['Trip Duration'].mean().round()
    print_pause(f"Average travel time is {averag_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_tybe=df['User Type'].value_counts()
    print_pause(f"User Types are : \n {User_tybe}")

    # TO DO: Display counts of gender
    try:
        gender_tybe=df['Gender'].value_counts()
        print_pause(f'Gender Types are : \n {gender_tybe}')
    except:
        print_pause("There are no Gender data in this city !! ")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year=df['Birth Year'].min()
        print_pause(f"The earliest year of birth is : {earliest_year}")
    except:
        print_pause("There are no Birth Year data in this city")
      
    try:
        most_recent_year=df['Birth Year'].max()
        print_pause(f"The most recent year of birth is : {most_recent_year}")
    except:
        print_pause("There are no Birth Year data in this city")
      
    try:
        most_common_year=df['Birth Year'].mode()[0]
        print_pause(f"The most common year of birth is : {most_common_year}")
    except:
        print_pause("There are no Birth Year data in this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while True:
        if view_data=='yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_display = input("Do you wish to continue?: ").lower()
            if view_display == 'no':
                break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())

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
