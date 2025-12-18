#get the special phrase from the user and perform string manipulations
str_manip = input("please enter a qoute you love:\n")

str_length = len(str_manip)

print(str_length)

last_character = str_manip[-1]

print(last_character)

print(str_manip.replace(last_character, "@"))

print(str_manip[-3:][::-1])

print(str_manip[0:2] + str_manip[-3:])


