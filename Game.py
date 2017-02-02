#!/usr/bin/python

import sys
import HotelClass

print "Work in progress..."

#setting up new game...
try:
    if int(sys.argv[1]) == 1:
        print "Selecting normal difficulty."
        hotel = HotelClass.Hotel(1)
    if int(sys.argv[1]) == 2:
        print "Selecting hard difficulty."
        hotel = HotelClass.Hotel(2)
    if int(sys.argv[1]) > 2:
        print "Higher value than 2 detected, defaulting to normal difficulty."
        hotel = HotelClass.Hotel(1)
except ValueError:
    print "No valid value was given, defaulting to normal difficulty."
    hotel = Hotel(1)

#printing difficulty
print hotel.difficulty
