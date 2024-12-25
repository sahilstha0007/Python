user_input = str(input("Enter date in a format mm/dd/yyyy: "))
month, day, year = user_input.split('/')

def month_finder(value):
    #months is used as a lookup table
    months = "JanFebMarAprMayJunoJulAugSepOctNovDec"
    #compute starting position of month n in months
    pos = (int(value)-1) * 3
    #Grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]
    return monthAbbrev
print("The conversion of this {0} is {1} {2}, {3}. " .format(user_input,month_finder(month),day,year))