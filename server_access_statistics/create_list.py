#!/usr/bin/env python
"""
Create a list with random user logins in the following format:
139.18.150.185 16:02:08 Friday
139.18.150.150 13:36:50 Friday
139.18.150.126 9:32:16 Tuesday
"""

from random import choice, randrange
from datetime import timedelta


def get_entry():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return f'139.18.150.{randrange(100, 200)} {timedelta(seconds=randrange(0, 86400))} {choice(days)}'


file = open("statistics.txt", "w+")
for _ in range(300):
    file.write(f'{get_entry()}\n')
file.close()
