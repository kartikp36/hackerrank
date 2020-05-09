inWords = [0,"one","two","three","four","five","six","seven","eight","nine","ten", "eleven", "twelve" ,"thirteen" ,"fourteen" ,15 ,"sixteen" ,"seventeen" ,"eighteen" ,"nineteen" ,"twenty" ,"twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine"]

hour = int(input())
minutes = int(input())
if minutes <= 30:
    if minutes == 0:
        print(inWords[hour]+" o' clock")
    elif minutes == 15:
        print("quarter past "+inWords[hour])
    elif minutes == 30:
        print("half past "+inWords[hour])
    else:
        if minutes == 1:
            print(inWords[minutes]+" minute past "+inWords[hour])
        else:
            print(inWords[minutes]+" minutes past "+inWords[hour])
else:
    hour += 1
    if minutes == 45:
        print("quarter to "+inWords[hour])
    else:
        minutes = 60 - minutes
        print(inWords[minutes]+" minutes to "+inWords[hour])
