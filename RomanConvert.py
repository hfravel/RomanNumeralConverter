romanNums = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

shortRomans = ("I", "V", "X", "L", "C", "D", "M")
romans = ( "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
integs = (1000,  900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1)

def romanToInt(num):
    total = 0
    prev = 9999
    curr = 0
    repeat = 0
    
    # Loops through each character of the string num
    for x in num:
        # If there is a character that is not I, V, X, L, C, D, or M then it is not valid.
        if x not in shortRomans:
            total = 0
            break
        
        # Saves the curr value of the current letter
        curr = romanNums[x]
        
        # Checks whether the curr is equal, less, or greater than last one.
        if prev == curr:
            repeat += 1
            # If it is repeated more than 3 times this is an invalid number.
            if repeat > 3:
                total = 0
                break
            #If a V, L, or D is placed next to itself then it is invalid.
            elif (curr == 5 or curr == 50 or curr == 500) and repeat > 2:
                total = 0
                break
            # If neither of the previous are true then it is valid
            else:
                total += curr
        elif curr < prev:
            # This is simplest senario. ex. VI
            total += curr
            repeat = 1            
        else:
            # Repeat cannot be more than 1 because IX exists but IIX doesn't. 
            if repeat > 1:
                total = 0
                break
            # Because of hwo the patterns and math works out, the previous letter must be 1/5 or 1/10 or the current.
            elif (curr / prev == 5) or (curr / prev == 10):    
                total -= 2 * prev
                total += curr
                repeat = 1
            # If neither of the above two are true then this roman numeral is a fake one.
            else:
                total = 0
                break

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
            if num >= integs[x]:
                #if it is divisible, to save time why not add it that many times.
                amt = num / integs[x]
                romanNum += romans[x] * amt
                num -= integs[x] * amt
                break
    
    return romanNum


#Start of testing area
tot = True
for i in range(1, 4000):
    r = intToRoman(i)
    n = romanToInt(r)
    if n!= i:
        print("{}: {}: {}.".format(i, r, n))
print("Successful 1-3999 loop if not print statements above.")

for x in romanNums:
    print(x)

number = raw_input("Give a Roman Numeral: ")
while number != "q":
    ans = romanToInt(number)
    if ans == 0:
        print("Invalid: {}.".format(number))
    else:
        print("Roman: {}, Number: {}.".format(number, ans))
    number = raw_input("Give a Roman Numeral: ")
