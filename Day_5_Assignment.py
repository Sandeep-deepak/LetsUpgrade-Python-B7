print("Question 1: ")
# Write a program to identify sub list [1,1,5] is there in the given list in the same order, if yes print 
# “it’s a Match” ​if no then print ​“it’s Gone” ​in function.
# Example -  Listy =[1,5,6,4,1,2,3,5] - ​it’s a Match , ​Listy = [1,5,6,5,1,2,3.6] - ​it’s Gone 

sublst=[1,1,5]
def sublist(lis):
    a=0
    count=0
    for item in sublst:
        for i in range(a, len(lis)):
            if item==lis[i]:
                a=i+1
                count+=1
                break
    if count ==len(sublst):
        print("its Match")
    else:
        print("its Gone")
listy = [1,5,6,4,1,2,3,5]
listy1 = [1,5,6,5,1,2,3.6]
sublist(listy)
sublist(listy1)



print("Question 2: ")
# Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500 

print("Prime numbers between 1 and 2500 are: ")
lst = list(range(1,2500))
def prime(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                break  
        else:  
            return num 
lst_prime = filter(prime,lst)
print(list(lst_prime))


print("Question 3: ")
# Make a Lambda function for capitalizing the whole sentence passed using arguments. 
# And map all the sentences in the List, with the lambda functions
# [“hey this is sai”,I am in mumbai”,....]
# o/p- [“Hey This Is Sai”, I Am In Mumbai”,....] 

info = ["hey this is sandeep","i live in vizag"]
details = list(map(lambda x: x.title(),info))
print(details)






