import pywhatkit


# Line 6 to 10 for personal number

number = input("Enter phone number with country code")
message = input("Enter message to be delivered")
time_hrs = int(input("Enter hours (in 24hr format)"))
time_mins = int(input("Enter mins"))
pywhatkit.sendwhatmsg(number, message, time_hrs, time_mins, 15, True, 3)

# Line 14 to 18 for groups

group_ID = input("Enter group ID")
message = input("Enter message to be delivered")
time_hrs = int(input("Enter hours (in 24hr format)"))
time_mins = int(input("Enter mins"))
pywhatkit.sendwhatmsg_to_group(group_ID, message, time_hrs, time_mins, 15, True, 3)


# comment out the one which is not being used i.e. any one of group or personal number
