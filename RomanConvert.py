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

def romanToInt(num):
    total = 0
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
tot = True
for i in range(1, 4000):
    r = intToRoman(i)
    n = romanToInt(r)
    if n!= i:
        print("{}: {}: {}.".format(i, r, n))
print("Successful 1-3999 loop if not print statements above.")


print(romanToInt(""))

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


# This is a really inefficient, illogical, and too long to run test for all possible combinations.
# There are 15 nested loops because the longest Roman Numeral possile is MMMDCCCLXXXVIII = 3888.
romanChars.insert(0, "")
for a1 in romanChars:
    for a2 in romanChars:
        for a3 in romanChars:
            for a4 in romanChars:
                for a5 in romanChars:
                    for a6 in romanChars:
                        for a7 in romanChars:
                            romTest = a1 + a2 + a3 + a4 + a5 + a6 + a7
                            rTITest = romanToInt(romTest)
                            if rTITest != 0 and rTITest < 4000:
                                iTRTest = intToRoman(rTITest)
                                if iTRTest != romTest:
                                    print("Test Roman: {}, Result: {}, Result's Result: {}".format(romTest, rTITest, iTRTest))
#                            for a8 in romanChars:
#                                for a9 in romanChars:
#                                    for aa in romanChars:
#                                        for ab in romanChars:
#                                            for ac in romanChars:
#                                                for ad in romanChars:
#                                                    for ae in romanChars:
#                                                        for af in romanChars:
#                                                            romTest = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + aa + ab + ac + ad + ae + af
#                                                            rTITest = romanToInt(romTest)
#                                                            if rTITest != 0 and rTITest < 4000:
#                                                               iTRTest = intToRoman(rTITest)
#                                                               if iTRTest != romTest:
#                                                                   print("Test Roman: {}, Result: {}, Result's Result: {}".format(romTest, rTITest, iTRTest))
