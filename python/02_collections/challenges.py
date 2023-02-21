import datetime

### QUESTION 1 ###
### You are building part of a ticket system that will allow anyone with an account to preorder an item
### but only one account is allowed to purchase an item when it is available. Since the system itself
### is not able to identify whether the account has already made a preorder for such item, you need to
### create a final list of the accounts that are unique for the system to retrieve before placing orders.
###
### Write out the function with the least amount of steps as possible

def get_unique_accounts(orders: list) -> list:
    return list(set(orders))

get_unique_accounts(['123124','3432432','123124','123124','2131243','5345232','3432432'])
# ['123124','3432432','2131243','5345232']



### QUESTION 2 ###
### Coming back to the system above, you were asked to build the system to handle different items being 
### ordered. Thus, the ask is to take a list of tuples where each user is preordering a certain
### item and instead return a dictionary where each value will contain the user and the value would be
### the list of items allowed to purchasae.
###
### Argument: List(Tuple(UserId, Item)) 
### E.g. 
### [('123124', 'pokemon'), ('3432432', 'digimon'), ('123124', 'pokemon'), ('123124', 'digimon'), ('5345232', 'pokemon')]
###
### Result: Dict(String, List())
### E.g.
### {
###     '123124':['pokemon', 'digimon'],
###     '3432432':['digimon'],
###     '5345232':['pokemon']
### }
def get_users_preorder(orders: list) -> list:
    orders_dict = {}
    for userid, item in orders:
        if userid not in orders_dict:
            orders_dict[userid]={item}
        else:
            orders_dict[userid].add(item)
    
    for userid, item in orders:
            orders_dict[userid] = list(orders_dict[userid])

    return orders_dict

get_users_preorder([('123124', 'pokemon'), ('3432432', 'digimon'), ('123124', 'pokemon'), 
    ('123124', 'digimon'),('5345232', 'pokemon'),('2131243', 'medabots'),('2131243', 'digimon'),
    ('123124', 'pokemon'),('123124', 'gundam'),('5345232', 'gundam')])



### QUESTION 3 ###
### You are building a planning app that will allow a user to determine how many hours they have to spend
### at each location of their trip broken down between Morning, Afternoon, Evening and Night. The app has
### hardcoded the period of times to be the following:
### Morning: 8:00 AM to 12:00 PM
### Afternoon: 12:00 PM to 4:00 PM
### Evening: 4:00 PM to 8:00 PM
### Night: 8:00 PM to 12:00 AM
### The caller of your function will submit a list of dictionary values containing the location, start time
### and end time of that trip. Your function should return a nested dictionary containing the hours alloted 
### for each period interval for each location.
###
### Argument: List(Dict())
### E.g.
### [
###     {
###         "location": "Paris",
###         "start_time": datetime.datetime(year=2023, month=9, day=12, hour=12),
###         "end_time": datetime.datetime(year=2023, month=9, day=15, hour=9)
###     },
###     {
###         "location": "Brussels",
###         "start_time": datetime.datetime(year=2023, month=9, day=15, hour=11),
###         "end_time": datetime.datetime(year=2023, month=9, day=19, hour=9)
###     },
###     {
###         "location": "Berlin",
###         "start_time": datetime.datetime(year=2023, month=9, day=19, hour=12),
###         "end_time": datetime.datetime(year=2023, month=9, day=25, hour=10)
###     },
### ]
###
### Results: Dict(Dict())
### {
###     'Paris': {
###         "Morning": 13,
###         "Afternoon": 11,
###         "Evening": 14,
###         "Night": 17
###     },
###     'Brussels': {
###         "Morning": 13,
###         "Afternoon": 11,
###         "Evening": 14,
###         "Night": 17
###     },
###     'Berlin': {
###         "Morning": 13,
###         "Afternoon": 11,
###         "Evening": 14,
###         "Night": 17
###     }
### }
### Note: The times is the result answer are made up to show the expected format.

def get_trip_breakdown(schedule: list(dict())):
    schedule_dicti = {}
    for place in schedule:
        breakdown = {"Morning":0, "Afternoon":0, "Evening":0, "Night":0}
        schedule_dicti[place["location"]] = breakdown
        timediff = place['end_time'] - place['start_time']
    
        #add 4 hours per section per day
        for section in schedule_dicti[place["location"]]:
            schedule_dicti[place["location"]][section] += (4 * timediff.days)

        arrive_hour = place['start_time'].hour - 8
        depart_hour = place['end_time'].hour - 8

        #add hours to section based on the first day
        if arrive_hour != depart_hour:
            if arrive_hour < 4:
                schedule_dicti[place["location"]]['Morning'] += (4 - (arrive_hour % 4))
                schedule_dicti[place["location"]]['Afternoon'] += 4
                schedule_dicti[place["location"]]['Evening'] += 4
                schedule_dicti[place["location"]]['Night'] += 4
            elif arrive_hour < 8:
                schedule_dicti[place["location"]]['Afternoon'] += (4 - (arrive_hour % 4))
                schedule_dicti[place["location"]]['Evening'] += 4
                schedule_dicti[place["location"]]['Night'] += 4
            elif arrive_hour < 12:
                schedule_dicti[place["location"]]['Evening'] += (4 - (arrive_hour % 4))
                schedule_dicti[place["location"]]['Night'] += 4
            elif arrive_hour < 16:
                schedule_dicti[place["location"]]['Night'] += (4 - (arrive_hour % 4))

        #subtract hours based on last day since it would be double counted if arrival hour is before departure hour
        if arrive_hour < depart_hour:
            if depart_hour < 4:
                schedule_dicti[place["location"]]['Morning'] -= (4 - (depart_hour % 4))
                schedule_dicti[place["location"]]['Afternoon'] -= 4
                schedule_dicti[place["location"]]['Evening'] -= 4
                schedule_dicti[place["location"]]['Night'] -= 4
            elif depart_hour < 8:
                schedule_dicti[place["location"]]['Afternoon'] -= (4 - (depart_hour % 4))
                schedule_dicti[place["location"]]['Evening'] -= 4
                schedule_dicti[place["location"]]['Night'] -= 4
            elif depart_hour < 12:
                schedule_dicti[place["location"]]['Evening'] -= (4 - (depart_hour % 4))
                schedule_dicti[place["location"]]['Night'] -= 4
            elif depart_hour < 16:
                schedule_dicti[place["location"]]['Night'] -= (4 - (depart_hour % 4))

        #add hours based on last day since it would not be accounted for if arrival hour is after departure hour
        elif arrive_hour > depart_hour:
            if depart_hour < 4:
                schedule_dicti[place["location"]]['Morning'] += depart_hour % 4  
            elif depart_hour < 8:
                schedule_dicti[place["location"]]['Morning'] += 4
                schedule_dicti[place["location"]]['Afternoon'] += depart_hour % 4
            elif depart_hour < 12:
                schedule_dicti[place["location"]]['Morning'] += 4
                schedule_dicti[place["location"]]['Afternoon'] += 4
                schedule_dicti[place["location"]]['Evening'] += depart_hour % 4
            elif depart_hour < 16:
                schedule_dicti[place["location"]]['Morning'] += 4
                schedule_dicti[place["location"]]['Afternoon'] += 4
                schedule_dicti[place["location"]]['Evening'] += 4
                schedule_dicti[place["location"]]['Night'] += depart_hour % 4

    return schedule_dicti


def get_trip_breakdown_2(schedule: list(dict())):
    trip_plan = {}
    for trip in schedule:
        location = trip["location"]
        trip_plan[location] = {}
        total_hours = (int)((trip["end_time"] - trip["start_time"]).total_seconds() / 3600)
        offset = trip["start_time"].hour
        if(offset <= 8):
            midnight = -offset
            morning = 0
            afternoon = 0
            evening = 0
            night = 0
        elif(offset > 8 and offset <= 12):
            midnight = -8
            morning = 8 - offset
            afternoon = 0
            evening = 0
            night = 0
        elif(offset > 12 and offset <= 16):
            midnight = -8
            morning = -4
            afternoon = 12 - offset
            evening = 0
            night = 0
        elif(offset > 16 and offset <= 20):
            midnight = -8
            morning = -4
            afternoon = -4
            evening = 16 - offset
            night = 0
        else:
            midnight = -8
            morning = -4
            afternoon = -4
            evening = -4
            night = 20 - offset
        
        total_offseted_hours = total_hours + offset
        while(True):
            # Midnight
            if (bool((int)(total_offseted_hours / 8))):
                midnight += 8
                total_offseted_hours -= 8
            else:
                midnight += total_offseted_hours
                total_offseted_hours = 0
                break

            # Morning
            if (bool((int)(total_offseted_hours / 4))):
                morning += 4
                total_offseted_hours -= 4
            else:
                morning += total_offseted_hours
                total_offseted_hours = 0
                break

            # Afternoon
            if (bool((int)(total_offseted_hours / 4))):
                afternoon += 4
                total_offseted_hours -= 4
            else:
                afternoon += total_offseted_hours
                total_offseted_hours = 0
                break

            # Evening
            if (bool((int)(total_offseted_hours / 4))):
                evening += 4
                total_offseted_hours -= 4
            else:
                evening += total_offseted_hours
                total_offseted_hours = 0
                break

            # Night
            if (bool((int)(total_offseted_hours / 4))):
                night += 4
                total_offseted_hours -= 4
            else:
                night += total_offseted_hours
                total_offseted_hours = 0
                break

        trip_plan[location]["Morning"] = morning
        trip_plan[location]["Afternoon"] = afternoon
        trip_plan[location]["Evening"] = evening
        trip_plan[location]["Night"] = night

    return trip_plan

print(get_trip_breakdown_2([
    {
        "location": "Paris",
        "start_time": datetime.datetime(year=2023, month=9, day=12, hour=13),
        "end_time": datetime.datetime(year=2023, month=9, day=12, hour=19)
    },
    {
        "location": "Brussels",
        "start_time": datetime.datetime(year=2023, month=9, day=15, hour=11),
        "end_time": datetime.datetime(year=2023, month=9, day=19, hour=9)
    },
    {
        "location": "Berlin",
        "start_time": datetime.datetime(year=2023, month=9, day=19, hour=12),
        "end_time": datetime.datetime(year=2023, month=9, day=25, hour=10)
    },
]))


# {
#    "Paris":{
#       "Morning":9,
#       "Afternoon":12,
#       "Evening":12,
#       "Night":12
#    },
#    "Brussels":{
#       "Morning":14,
#       "Afternoon":16,
#       "Evening":16,
#       "Night":16
#    },
#    "Berlin":{
#       "Morning":22,
#       "Afternoon":24,
#       "Evening":24,
#       "Night":24
#    }