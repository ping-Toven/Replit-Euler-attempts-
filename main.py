# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

threelessthan, fivelessthan, sum = True, True, 0

for i in range(1000):
  while (threelessthan):
    print("lol")
    threex = 3 * i
  while (fivelessthan):
    fivex = 5 * i
  if threex > 1000:
    threelessthan = False
    killswitch1 = True
    print("ks1")
    continue
  sum += threex
  print("3 x ")
  print(i)
  if fivex > 1000:
    fivelessthan = False
    killswitch2 = True
    print("ks2")
    continue
  sum += fivex
  print ("5 x ")
  if killswitch1 and killswitch2:
    break

print("The sum of all the multiples of 3 or 5 below 1000 is: ")
print(sum)