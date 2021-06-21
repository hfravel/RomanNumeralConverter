romanNums = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def romanConvert(num):
    total = 0
    prev = 0
    curr = 0
    repeat = 0
    
    for x in num:
       
        curr = romanNums[x]
        
        if prev == curr:
            repeat += 1
            if repeat > 3:
                total = 0
                break
            elif (curr == 5 or curr == 50 or curr == 500) and repeat > 2:
                total = 0
                break
            else:
                total += curr
        elif curr > prev:
            total += curr
            repeat = 1            
        else:
            if total > curr:
                total = 0
                break
            elif repeat > 1:
                total = 0
                break
            else:
                total -= 2 * curr
                repeat = 1

        prev = curr
    
    print(total)

number = raw_input("Give a Roman Numeral: ")
romanConvert(number)
