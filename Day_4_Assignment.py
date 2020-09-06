# Question 1
'''Print the first ArmStrong(Narcissistic) number in the range of 1042000 to 702648265 and exit the loop
as soon as you encounter the first armstrong number. ---Use while loop---'''
# Armstrong number is a number that is equal to the sum of the cubes(for 3 digit number) of its own digits.
# abc = a**n + b**n + c**n ;  n = length of digits(abc)

for num in range(1042000, 702648266):
   sum = 0 # initialize sum
   temp = num
   while temp > 0:
       digit = temp % 10 # Gives Remainder a
       sum += digit ** len(str(num)) # sum = sum + a**n
       temp //= 10 # Gives Quotient (without decimal point)
   if num == sum: # if condition is true then print
       print("The first Armstrong number is: ",num)
       break # breaks the loop after first if condition is true