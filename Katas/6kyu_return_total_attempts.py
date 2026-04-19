#6Kyu Kata... 

#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

#I have to take the nums that forms the main number, multiply them and, if the result of the multiplication has one digit, return the result, else keep doing this process until the result has one digit 

import math

def persistence(n):

    attempts = 0

    while len(str(n)) > 1:

        if len(str(n)) > 1:
            attempts += 1 

        numbers = []

        for i in str(n):
            numbers.append(int(i))

        n = math.prod(numbers)

        

    return attempts  
                
                
            
key = persistence(39)
print(key)