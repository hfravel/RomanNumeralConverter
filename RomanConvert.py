romanNums = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

romans = ( "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
romanInts = (1000,  900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1)
romanChars = ["I", "V", "X", "L", "C", "D", "M"]

# This function takes as input a string of roman numerals and turns
# it into an integer.
def romanToInt2(num):
    # total is for the final value, repeat is how many times a letter has 
    # been repeated curr is the current letter value, prev is the previous 
    # letter value, and pprev is the previous previous letter value.
    total = 0
    curr = 0
    prev = 0
    pprev = 0
    repeat = 0
    maxx = 9000
    numLen = len(num)
    
    # No roman numeral has a longer length than 15.
    if numLen > 15:
        return 0
    
    # If the roman numeral is (I, V, X, L, C, D, M)
    if numLen == 1:
        if num[0] in romanChars: return romanNums[num[0]]
        else: return 0

    # Deals with the base case of 0 and 1 which do not have both a prev and a pprev.
    # Yes this is duplicated code but I believe it saves on efficiency because 
    # there is not need for extra checking in the loop whether it is at 0 or 1.
    if num[0] in romanChars and num[1] in romanChars:
        pprev = romanNums[num[0]]
        prev = romanNums[num[1]]
        
        # Cases: (VI, XV, XI, LX, LV ... MX, MV, MI)
        # Further explained in the loop.
        if pprev > prev:
            repeat = 1
            total = prev + pprev
            maxx = pprev
        # Cases: (IV, IX, XL, XC, CD, CM)
        # Further explained in the loop.
        elif pprev < prev:
            if pprev in (1, 10, 100) and (prev / pprev in (5, 10)):
                repeat = 1
                total = prev - pprev
                maxx = prev
            else:
                return 0
        # Cases: (II, XX, CC, MM)
        # Further explained in the loop.
        else:
            if prev in (1, 10, 100, 1000):
                repeat = 2
                total = 2 * prev
                maxx = prev
            else:
                return 0
    else:
        return 0

    # Loops through all letters of num, and returns 0 for an invalid
    # roman numeral.
    for i in range(2, numLen):
        # Invalid character detection.
        if num[i] not in romanChars:
            return 0
        
        # Sets curr to the current value of the current letter.
        curr = romanNums[num[i]]
        

        # If the previous set of letter looks like this: (IV, IX, XL,
        # XC, CD, CM) then the curr letter must be less then the
        # previous letter.
        if pprev < prev:    
            if pprev > curr:
                repeat = 1
                total += curr
            else:
                return 0
        # The curr letter can only be greater than the prev one if it is
        # of the form (IV, IX, XL, XC, CD, CM).        
        elif prev < curr:
            if repeat > 1:
                return 0
            elif prev in (1, 10 ,100) and curr / prev in (5, 10):
                if curr > maxx or (curr == maxx and curr in (5, 50, 500)):
                    return 0
                else:
                    repeat = 1
                    total -= 2 * prev
                    total += curr
                    maxx = curr
            else:
                return 0
        # Easiest case: add to total and reset repeat value if curr is
        # less than prev.
        elif prev > curr:
            if curr > maxx:
                return 0
            else:
                repeat = 1
                total += curr
                maxx = prev
        # If curr is equal to prev then the letter cannot be repeated
        # more than 3 times and V, L, D cannot be repeated at all.
        elif prev == curr:
            if repeat >= 3 or curr in (5, 50, 500):
                return 0
            else:
                repeat += 1
                maxx = curr
                total += curr
        else:
            return 0
        
        # End of the loop so curr becomes prev and prev becomes pprev.
        pprev = prev
        prev = curr
    
    # If it makes it here the roman numeral value is stored in total
    # and there were no errors.
    return total



# Takes as input a integer and returns a string representing
# the roman numeral.
def intToRoman(num):
    romanlen = len(romans)
    result = ""
    
    #loops until the number is 0
    while num > 0:
        #Loops though the possible number combinations until one is equal to or less than
        for x in range(romanlen):
            if num >= romanInts[x]:
                #if it is divisible, to save time why not add it that many times.
                amt = num / romanInts[x]
                result += romans[x] * amt
                num -= romanInts[x] * amt
    
    return result


#Start of testing area

# This checks all the Roman Numerals in the range 1-3999 to see if my converters work.
tot = True
for i in range(1, 4000):
    r = intToRoman(i)
    n = romanToInt2(r)
    if n!= i:
        print("{}: {}: {}.".format(i, r, n))
        tot = False
if tot:
    print("Roman Numeral converters were successful for numbers 1-3999.")
else:
    print("Roman Numeral converters failed for numbers 1-3999.  See reasons above.")



"""
# This is the area where I tried my best to test certain errors by hand
# and was unable to find negative results.
number = raw_input("Give a Roman Numeral: ")
while number != "q":
    ans = romanToInt(number)
    if ans == 0:
        print("Invalid: {}.".format(number))
    else:
        print("Roman: {}, Number: {}.".format(number, ans))
    number = raw_input("Give a Roman Numeral: ")
"""

# The longest roman numeral is 15 digits. So D can be [2..16] looping through
# just 1 digit or all the way up to 15 digits.
D = 8
N = 7
for i in range(1, D):
    # There are seven possible roman numerals (I, V, X, L, C, D, M).
    # This loops through all possible combinations (this number system is close to base seven).
    for j in range (0, N**i):
        num = j
        romanNum = ""
        # This translates the base seven number into roman numerals.
        for k in range(i-1, -1, -1):
            numMod = num / (N**k)
            num = num % (N**k)
            romanNum += romanChars[numMod]
        resultInt = romanToInt2(romanNum)
        resultRom = intToRoman(resultInt)
        if (resultRom != romanNum and not (resultInt == 0 and resultRom == "")):
            print("Created: {}, Num: {}, Real: {}".format(romanNum, resultInt, resultRom))
        #print("Dig: {}; Num: {}; {}.".format(i, j, romanNum))

