class Location:
    def __init__(self, location):
        self.location = location
        self.activities = []

class Activity: 
    def __init__(self, activity):
        self.activity = activity
        self.locations = []

if __name__ == '__main__':
    #  create all location instance's
     location1 =  Location('miami')
     location2 =  Location('cuba')
     location3 =  Location('lake luis')
     location4 =  Location('philipines')
    #  create all activity instance's
     activity1 = Activity('clear water swimming')
     activity2 = Activity('ice skating')
     activity3 = Activity('cycling')
     activity4 = Activity('running')
     activity5 = Activity('hiking')
     activity6 = Activity('sauna')
    # link activities to locations
     location1.activities = [activity3, activity6]
     location2.activities = [activity1, activity3, activity4]
     location3.activities = [activity2, activity3, activity4, activity5]
     location4.activities = [activity1, activity4 ,activity5]
    # link locations to activities 
     activity1.location = [location2, location3, location4]
     activity2.location = [location2]
     activity3.location = [location1, location2]
     activity4.location = [location2, location3, location4]
     activity5.location = [location3, location4]
     activity6.location = [location1]

     print(f'These are the activities in (the) "{location3.location}":')
     for i, activity in enumerate(location3.activities):
         print(f'{i}: {activity.activity}')
         
     print()

     print(f'These are the locations that have "{activity1.activity}":')
     for i, location in enumerate(activity1.location):
         print(f'{i}: {location.location}')