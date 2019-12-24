import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months=['January','February', 'March', 'April','May', 'June']
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
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
    while True:
        try:
            #city name
            city=str(input('Would you like to see data for chicago, new york, or washington? \n')).lower()
            if city in  CITY_DATA:
                break
            else:
                print("wrong input ,check your code again")
        except:
            print("error")
        
    
    # get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            # input month 
            month=str(input('would you like to filter the data by month (yes or no)? \n')).lower()
            if month in ['no','yes']:            
                if month == 'no':
                    month='all'
                    break
                elif month == 'yes':
                    while True:                    
                        month=str(input('choose a month? January, February, March, April, May, or June?\n')).title()
                        if month in months:
                            break
                        else: 
                            print("wrong input")
                    break
            else:
                print("wrong input")
        except:
            print("wrong input")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            #filter by name 
            day=str(input('would you like to filter the data by day (yes or no)? \n')).lower()
            if day in ['yes','no']:
                if day == 'no':
                    day = 'all'
                    break
                elif day == 'yes':
                    while True: 
                        day=str(input('choose a  day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday \n')).title()
                        if day in days:
                            break
                        else:
                            print("wrong input ,check your code again")
                    break
            else:
                print("wrong input")
        except:
            print("wrong input,check your code again")       
      
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
        df - pandas DataFrame containing city data filtered by month and day
    """
    #read csv file 
    df = pd.read_csv(CITY_DATA[city])

    #convert to date time 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #creat month column
    df['month'] = df['Start Time'].dt.month
    #creat day column
    df['day'] = df['Start Time'].dt.weekday_name
    #creat hour column
    df['hour']=df['Start Time'].dt.hour


    if month != 'all':
        month =months.index(month.title())+1
    

        df = df[df['month'] == month]

    
    if day != "all":
       
        df = df[df['day']==day.title()]
    return df

 
 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month=df["month"].mode()[0]
    count_most_common_month=df["month"].value_counts()[most_common_month]

    # display the most common day of week
    most_common_day=df["day"].mode()[0]
    count_most_common_day=df["day"].value_counts()[most_common_day]
    # display the most common startour
    most_common_hour=df["hour"].mode()[0]
    count_most_common_hour=df["hour"].value_counts()[most_common_hour]
    
    print("The most common month: {}, Count {} \nThe most common day: {}, Count {} \nThe most common hour: {}, Count {}".format(months[most_common_month-1],count_most_common_month,most_common_day,count_most_common_day,most_common_hour,count_most_common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start_station=df["Start Station"].mode()[0]
    count_most_start_station=df["Start Station"].value_counts()[most_start_station]

    # display most commonly used end station
    most_end_station=df["End Station"].mode()[0]
    count_most_end_station=df["End Station"].value_counts()[most_end_station]

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + '&' + df['End Station']
    most_start_and_end_station= df['Start End'].value_counts().idxmax()
    #print(popular_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df["Trip Duration"].sum()


    # display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    
    print("Trip Duration: {} , mean travel time {}".format(total_travel_time,mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_types = df["user type"].value_counts()

    # Display counts of gender
    count_of_gender = df["gender"].value_counts()

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df["Birth Year"].min()
    most_recent_birth_year = df["Birth Year"].max()
    most_common_birth_year = df["Birth Year"].mode()[0]
    print("counts of user types \n{}\ncounts of gender \n{} \nThe earliest birth year is: {}\nTne most recent birth year is {}\nThe most common birth year is {}".format(counts_user_types,count_of_gender,earliest_birth_year,most_recent_birth_year,most_common_birth_year))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# get_filters()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if "gender" in df:
            user_stats(df)
        head = 0
        size = 4
        #handle data view
        while True:
            try:
                view_trip_data = str(input("Would you like to see individual trip data? (yes or no)\n")).lower()
                if view_trip_data in ['yes','no']:
                    if view_trip_data =='yes':
                        print(df.loc[head:head+size])
                        head+=size+1
                    else:
                        break
                else: 
                    print("wrong input")  
            except:
                print("wrong input")
        check = 0        
        while True:        
            try:
                restart = input("\nWould you want to restart? Enter yes or no.\n").lower()
                if restart in ["yes","no"]:
                    if restart == "yes": 
                        check=1
                        break
                    elif restart == "no":
                        check=0
                        break
                else:
                    print(" wrong input check your code again ")
            except:
                print("wrong input check your code again")
        if check==0:
            break
                
        
if __name__ == "__main__":
    main()
