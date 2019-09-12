"""
Three simple functions that convert from one value to another
Willie Alber 9/12/2019
"""


# Takes two inputs, (base and height), which should be floats and returns the area.
# This function assumes that all values are positive.
def area(base, height):
    print(.5*(base*height))


# Takes three inputs, which should be floats, and returns the volume.
# This function assumes that all values are positive.
def volume(base, height, width):
    print(base*height*width)


# Takes a distance measurement, then asks you to define what type of measurement it is.
# Will return a small table containing centimeter/inch/foot/meter conversions.
# Assumes that the float value given will be positive.
def measure(distance):
    t = input("What type of measurement do you have? [centimeter/inch/foot/meter] ")
    distance = float(distance)
    if t == "centimeter":
        cent_inch = round(distance * .393701, 3)
        cent_foot = round(distance * .0328084, 3)
        cent_meter = round(distance * .01, 3)
        print("Conversion table for " + str(distance) + " centimeters:")
        print("Value in Inches: " + str(cent_inch))
        print("Value in Feet: " + str(cent_foot))
        print("Value in Meters: " + str(cent_meter))
    elif t == "inch":
        inch_cent = round(distance * 2.54, 3)
        inch_foot = round(distance * .08333, 3)
        inch_meter = round(distance * .0254, 3)
        print("Conversion table for " + str(distance) + " inches:")
        print("Value in Centimeters: " + str(inch_cent))
        print("Value in Feet: " + str(inch_foot))
        print("Value in Meters: " + str(inch_meter))
    elif t == "foot":
        foot_cent = round(distance * 30.48, 3)
        foot_inch = round(distance * 12, 3)
        foot_meter = round(distance * .3048, 3)
        print("Conversion table for " + str(distance) + " feet:")
        print("Value in Centimeters: " + str(foot_cent))
        print("Value in Inches: " + str(foot_inch))
        print("Value in Meters: " + str(foot_meter))
    elif t == "meter":
        meter_cent = round(distance * 100, 3)
        meter_inch = round(distance * 39.3701, 3)
        meter_foot = round(distance * 3.28084, 3)
        print("Conversion table for " + str(distance) + " meters:")
        print("Value in Centimeters: " + str(meter_cent))
        print("Value in Inches: " + str(meter_inch))
        print("Value in Feet: " + str(meter_foot))
    else:
        return "Invalid variable entry. Please try again."


print(area(15, 12))
print(volume(12, 16, 4))
print(measure(5.5))
