#!/usr/bin/env python
"""
Script that processes a list of user logins in the following format:
139.18.150.185 16:02:08 Friday
139.18.150.150 13:36:50 Friday
139.18.150.126 9:32:16 Tuesday

The output is in the following format:
139.18.150.181
Total visits: 6
Most popular day/s: 3 visit/s on Monday
Most popular hour/s: 2 visit/s at 10
"""


from collections import Counter


# Find the max visits for an item(hours, days).
def get_max_visits(items):
    return max([visits[1] for visits in Counter(items).most_common()])


# Find the item/s(hours, days) with max visits.
def find_items_with_max_visits(items):
    max_visits = get_max_visits(items)
    most_common = []
    for item in Counter(items).most_common():
        if item[1] == max_visits:
            most_common.append(item[0])
    return most_common


data = {}
r_file = open("statistics.txt", "r")
# Add all the data into a nested dictionary with the IP as a key
for line in r_file:
    ip, time, day = line.split()
    # Grab only the hours as we do not need the minutes and seconds
    hours = time.split(':')[0]
    if ip not in data:
        data[ip] = {'time': [hours], 'day': [day]}
        continue
    data[ip]['time'].append(hours)
    data[ip]['day'].append(day)
r_file.close()

w_file = open('processed_stats.txt', 'w+')
for key, value in data.items():
    # Append the days if there are more than one with the maximum number of visits.
    max_visits_in_a_day = get_max_visits(value["day"])
    most_common_days = find_items_with_max_visits(value["day"])

    # Do the same for the hours of the day.
    max_visits_in_an_hour = get_max_visits(value["time"])
    most_common_hours = find_items_with_max_visits(value["time"])

    w_file.write(f'{key}\n'
                 f'Total visits: {len(value["time"])}\n'
                 f'Most popular day/s: {max_visits_in_a_day} visit/s on {", ".join(most_common_days)}\n'
                 f'Most popular hour/s: {max_visits_in_an_hour} visit/s at {", ".join(most_common_hours)}\n\n')

# Find the hour with most overall visits
total_hours = []
for _, value in data.items():
    total_hours.extend(value['time'])

total_max_visits_in_an_hour = get_max_visits(total_hours)
hours_with_max_visits = find_items_with_max_visits(total_hours)

w_file.write(f'{"-"*10}\n'
             f'Most popular overall hour/s: {total_max_visits_in_an_hour} visits at {", ".join(hours_with_max_visits)}')
w_file.close()
