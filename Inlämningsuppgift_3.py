from datetime import datetime, timedelta
import math
import time
import os
from types import NoneType


def cls():
    #Funktion för att rensa konsollen
    os.system('cls' if os.name=='nt' else 'clear')
 
def round_down_to_nearest_half_int(num):
    #Funktion som senare kommer avrunda timmarna till halvor (exempel:'1,5', '1.0' '8,5')
    #Använder math.floor för att avrunda timmarna nedåt
    return math.floor(num * 2) / 2

def get_wage():
    #Funktion som ber användaren om deras timlön
    while True:
        try:
            hourly_wage = int(input("\nWhat is your hourly wage?: "))
            return hourly_wage
        except ValueError:
            print("\nInvalid amount")

def get_weekday():
    #Funktion som redogör viken dag det är
    weekdays_dict = {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"
                }
    day = 0
    while day < 1 or day > 7:
        try:
            day = int(input("\nWhat day is it? ('Monday' = 1,), (1-7): "))
        except ValueError:
            print("\nEnter a number")
    for i in weekdays_dict:
        if i == day:
            weekday = weekdays_dict[day]
    return weekday

def get_hours():
    #Få ut differensen mellan arbetstimmarna
    while True:
        try:
            start_time = input("Enter time for start of workday.('00:00'): ")
            end_time = input("\nEnter time for end of workday.('00:00'): ")
            time_format = '%H:%M'
            diff = timedelta
            #Om man jobbar skriver att man jobbar över 24:00
            if start_time > end_time:
                print("You can't overlap workdays. Program will restart in 3 seconds...")
                time.sleep(3)
                cls()
                break
            #Differensen mellan sluttiden och starttiden
            else:    
                diff = datetime.strptime(end_time, time_format) - datetime.strptime(start_time, time_format)
            #Vi får ut differensen i sekunder och omvandlar till timmar
            hour_diff = diff.total_seconds() / 3600
            #Om man jobbar över 12 timmar 
            if hour_diff > 12:
                hour_diff = 12
                print("\nYou will not recieve additional payment for work over 12 hours.")
                return hour_diff
        except ValueError:
            #datetime tillåter inte 24:00 utan bara 00:00....
            if end_time == "24:00":
                print("You can only be paid till 23:59\n")
            else:
                print("\nInvalid time")
        except AttributeError:
            print("You can only be paid till 23:59\n")
        else:
            return round_down_to_nearest_half_int(hour_diff)
    
def get_payment():
    work_hours = get_hours()
    while type(work_hours) == NoneType:
        work_hours = get_hours()
    hourly_wage = get_wage()
    weekday = get_weekday()
    hardship_time = work_hours - 8
    hourly_multiplier = 1
    
    #Räkna ut ob om det är helg
    if weekday == "Saturday" or weekday == "Sunday":
        hourly_multiplier = 2
   
    #Räkna ut ob för arbete över 8 timmar. OBS inte på helger
    if work_hours > 8 and hourly_multiplier != 2:
        hourly_multiplier = 1.5
        payment = hourly_wage * 8 + (hourly_wage * hourly_multiplier * hardship_time)
    else:
        payment = hourly_wage * work_hours * hourly_multiplier
    
    print(f"\nYou are being paid for {work_hours} hours on a {weekday} with a hourly wage"\
        f" of {hourly_wage} kr.\n\nYour salary for the day is: {payment} kr.")

get_payment()