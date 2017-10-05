
Def FizzBuzz(i):
  for i in range(1,101):  #Look for a number that is between 2 and 100
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:      #Can it be divided by 3?
        print("Fizz")
    elif i % 5 == 0:      #Can it be divided by 5
        print("Buzz")
    else:
        return i

      
       
