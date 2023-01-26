import time
import pandas as pd
import numpy as np
#import math as ma

CITY_DATA = {'chicago':'chicago.csv',
			  'new york city': 'new_york_city.csv',
			  'washington':'washington.csv'}


MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']

def get_filters():

	print("Hello! Lets explore some US Bikeshare data!!")
	# To get input for city name
	city_name = ' '
	while city_name.lower() not in CITY_DATA:
		city_name=input("\nPlease enter the city name to analyse data-Chicago, New york city, Washington\n")
		if city_name.lower() in CITY_DATA:
			city=CITY_DATA[city_name.lower()]
		else:
			print("\nSorry we dint recive an input. Please select the city -Chicago, New york city, Washington\n")

	month_name = ' '

	while month_name.lower() not in MONTH_DATA:
 		month_name=input("\nEnter the month name to filter-January,Febraury,..., June or all for no filter\n")
 		if month_name.lower() in MONTH_DATA:
 			month=month_name.lower()
 		else:
 			print("\nSorry we dint recive an input. Please enter month name to filter-January to June or all for no filter\n")

	day_name = ' '
	while day_name.lower() not in DAY_DATA:
 		day_name=input("\nEnter the day to filter- Sunday,Monday,...,Saturday or all for no filter\n")
 		if day_name.lower() in DAY_DATA:
 			day=day_name.lower()
 		else:
 			print("\nSorry we dint recive an input.Please enter the day to filter- Sunday,Monday,...,Saturday or all for no filter\n")
	print('-'*40)
	return city,month,day

def load_data(city, month, day):
    
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month ,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
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

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print("The most common month from the given data is: " + MONTH_DATA[most_common_month].title())

    # TO DO: display the most common day of week
    common_day_of_week=df['day_of_week'].mode()[0]
    print("The most common day of week from the given data is: " + str(common_day_of_week))

    # TO DO: display the most common start hour
    common_start_hour=df['hour'].mode()[0]
    print("The most common start hour from the given data is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
	"""Displays statistics on the most popular stations and trip."""

	print('\nCalculating The Most Popular Stations and Trip...\n')
	start_time = time.time()

	# TO DO: display most commonly used start station
	most_common_start_station=df['Start Station'].mode()[0]    
	print("The most common start station is  :  "+str(most_common_start_station))

	# TO DO: display most commonly used end station
	most_common_end_station=df['End Station'].mode()[0]
	print("The most common end station:  "+str(most_common_end_station))

	# TO DO: display most frequent combination of start station and end station trip
	frequent_combination = (df['Start Station']+"||"+df['End Station']).mode()[0]
	print("The most frequent combination of start station and end station:  "+str(frequent_combination.split("||")))

	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total trip duration is :  "+str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("Average trip duration is : " +str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    display_count=df['User Type'].value_counts()
    print("User type count is : \n" +str(display_count))

    # TO DO: Display counts of gender
    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
    	gender_count = df['Gender'].value_counts()
    	print("Gender count is : \n"+str(gender_count))
    else:
    	print("Gender data for this city is not given")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'chicago.csv' or city == 'new_york_city.csv':
    	earliest_year=df['Birth Year'].min()
    	print("The earliest year from the given data is :\n",int(earliest_year))
    	most_recent_year=df['Birth Year'].max()
    	print("The most recent year from the given data is:\n",int(most_recent_year))
    	common_year_birth=df['Birth Year'].mode()[0]
    	print("The most common year from the given data is: \n",int(common_year_birth))
    else:
    	print("Birth Year is not given for this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
	'''Display the raw data if user wants to'''

	print(df.head())
	count= 0
	while True:
		raw_data=input("Do you want to print the next five rows - Yes/No:\n")
		if raw_data.lower()=='yes':
			count=count+5
			print(df.iloc[count:count+5])
		else:
			break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
        	raw_data=input("Would like to see the first five rows of raw data -Yes/No: \n")
        	if raw_data.lower() != 'yes':
        		break
        	display_raw_data(df)
        	break
        	
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()




