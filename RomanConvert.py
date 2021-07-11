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
    
    # Loops through all letters of num, and returns 0 for an invalid
    # roman numeral.
    for i in range(0, numLen):
        # Invalid character detection.
        if num[i] not in romanChars:
            return 0
        
        # Sets curr to the current value of the current letter.
        curr = romanNums[num[i]]
        
        # If the previous set of letter looks like this: (IV, IX, XL,
        # XC, CD, CM) then the curr letter must be less then the
        # previous letter.
        if i > 1 and pprev < prev and repeat < 2:
            if pprev > curr:
                repeat = 1
                total += curr
            else:
                return 0
        # The curr letter can only be greater than the prev one if it is
        # of the form (IV, IX, XL, XC, CD, CM).        
        elif prev < curr:
            if i == 0:
                repeat = 1
                total += curr
            elif repeat > 1:
                return 0
            elif prev in (1, 10 ,100) and curr / prev in (5, 10):
                if curr > maxx or (pprev == curr and curr in (5,50,500)) or (curr == maxx and curr in (5, 50, 500)):
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

"""
def romanToInt(num):
    total = 0
    pprev = 9999
    prev = 9999
    curr = 0
    repeat = 0
    currlow = 9999
    prevlow = 9999
    
    # Loops through each character of the string num
    for x in num:
        # If there is a character that is not I, V, X, L, C, D, or M then it is not valid.
        if x not in romanChars:
            total = 0
            break
        
        # Saves the curr value of the current letter
        curr = romanNums[x]
        
        if curr > prev:
            # Repeat cannot be more than 1 because IX exists but IIX doesn't. 
            if repeat > 1:
                total = 0
                break
            # Because of hwo the patterns and math works out, the previous letter must be 1/5 or 1/10 or the current.
            elif (curr / prev == 5 or curr / prev == 10) and prev not in [romanNums["V"], romanNums["L"], romanNums["D"]]:    
                # Cannot have DCD because this is the same as CM. So a 5 cannot come before a 4.
                if prevlow == curr and curr in [romanNums["V"], romanNums["L"], romanNums["D"]]:
                    total = 0
                    break
                # If the previous is false then we continue with normal operations.
                total -= 2 * prev
                total += curr
                repeat = 1
                
                prevlow = currlow
                currlow = curr - prev
            # If neither of the above two are true then this roman numeral is a fake one.
            else:
                total = 0
                break
        # Roman Numerals are supposed to be organized from greatest on left to least on right.
        # Ex. MMCM is alright because this is 1000, 1000, 900.  but MMCMM is not because that is 1000, 1000, 900, 1000
        elif curr > currlow:
            total = 0
            break
        # Checks whether the curr is equal, less, or greater than last one.
        elif prev == curr:
            repeat += 1
            # If it is repeated more than 3 times this is an invalid number.
            if repeat > 3:
                total = 0
                break
            #If a V, L, or D is placed next to itself then it is invalid.
            elif curr in [romanNums["V"], romanNums["L"], romanNums["D"]] and repeat > 1:
                total = 0
                break
            # If neither of the previous are true then it is valid
            else:
                total += curr
        else:
            # This is simplest senario. ex. VI
            total += curr
            repeat = 1

            prevlow = currlow
            currlow = curr

        # End of the loop where we assign previous to current
        prev = curr
    
    return total
"""

# Takes as input a integer and returns a string representing
# the roman numeral.
def intToRoman(num):
    romanlen = len(romans)
    romanNum = ""
    
    #loops until the number is 0
    while num > 0:
        #Loops though the possible number combinations until one is equal to or less than
        for x in range(romanlen):
            if num >= romanInts[x]:
                #if it is divisible, to save time why not add it that many times.
                amt = num / romanInts[x]
                romanNum += romans[x] * amt
                num -= romanInts[x] * amt
                break
    
    return romanNum


#Start of testing area

# This checks all the Roman Numerals in the range 1-3999 to see if my converters work.
for i in range(1, 4000):
    r = intToRoman(i)
    n = romanToInt2(r)
    if n!= i:
        print("{}: {}: {}.".format(i, r, n))
print("Successful 1-3999 loop if not print statements above.")


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
D = 9
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

