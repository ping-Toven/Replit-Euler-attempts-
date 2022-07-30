# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

threelessthan, fivelessthan, sum, killswitch1, killswitch2 = True, True, 0, False, False

for i in range(1000):
    if killswitch1 and killswitch2:
        print("killed")
        break
    while (threelessthan):
        threex = 3 * i
        sum += threex
        if threex > 1000:
            threelessthan = False
            killswitch1 = True
            break
        break
    while (fivelessthan):
        fivex = 5 * i
        sum += fivex
        if fivex > 1000:
            fivelessthan = False
            killswitch2 = True
            break
        break
print("The sum of all the multiples of 3 or 5 below 1000 is: ")
print(sum)
