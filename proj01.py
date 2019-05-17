############################################
# Computer Project #1
#
# Algorithm
#    prompts for input
#    input a float
#    conversions
#        convert rods to meters to miles
#        convert rods to furlongs
#        convert meters to feet
#        convert for known minutes to walk
#        convert to rods per minute
#        round all floating outputs 3 places
#    print outputs
############################################
num_str = input("Input rods: ")
float1 = float(num_str)

x = float1
x = round(x , 3)

c1 = x * 5.0292 #rods to meters
c2 = c1 / 1609.34 #meters to miles
c3 = x / 40 #rods to furlongs
c4 = c1 / 0.3048 #meters to feet
c5 = x / 60 * 60 #minutes to walk
c6 = ((c2 / 3.1)) * 60 #rods per minute

#rounds all floating outputs 3 places
c1 = round(c1, 3)
c2 = round(c2, 3)
c3 = round(c3, 3)
c4 = round(c4, 3)
c5 = round(c5, 3)
c6 = round(c6, 3)

print("You input",x , "rods." )

print("Conversions" )
print("Meters:",c1)
print("Feet:",c4)
print("Miles:",c2)
print("Furlongs:",c3)
print("Minutes to walk",c5 , "rods:",c6 )
