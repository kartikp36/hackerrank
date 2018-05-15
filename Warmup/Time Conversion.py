time = input().split(':')
hour = int(time[0])
minutes = int(time[1])
seconds = int(time[2][0:2])
ampm = time[2][2:4]

if ampm == "PM":
    if hour == 12:
        hour = 12
    else:hour+=12

else:
    if hour == 12:
        hour=0
# print(hour,minutes,seconds, sep=":")
print('%02d:%02d:%02d'%(hour, minutes, seconds))