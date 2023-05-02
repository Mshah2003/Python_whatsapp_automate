import pywhatkit

number = input("Enter phone number with country code")
message = input("Enter message to be delivered")
time_hrs = int(input("Enter hours (in 24hr format)"))
time_mins = int(input("Enter mins"))
pywhatkit.sendwhatmsg(number, message, time_hrs, time_mins, 15, True, 3)


group_ID = input()
pywhatkit.sendwhatmsg_to_group_instantly(group_ID, message, 15, True, 3)
