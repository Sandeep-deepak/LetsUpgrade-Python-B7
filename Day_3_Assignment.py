# Question 1 
'''You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is 1000ft, 
it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask the 
pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try later” '''

num_Input = input("Enter Altitude Value: ")
num = int(num_Input)
if num <= 1000:
    print("Safe to Land")
elif num > 1000 and num <= 5000:
    print("Bring down to 1000")
else:
    print("Turn Around")

# Question 2 
# Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE function. 

print("Prime numbers between 1 and 200 are:")
for num in range(1,200):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
