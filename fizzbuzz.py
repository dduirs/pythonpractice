# Write a program to output the first 100 FizzBuzz numbers

# if the number is divisible by 3 print Fizz
# if the number is divisible by 5 print Buzz
# if the number is divisible by 3 and 5 print FizzBuzz
# if the number is not divisible by 3, 5 or both, print number

x=1
while x < 100:
    if (x % 15) == 0:
        print("FizzBuzz")
    elif (x % 3) == 0:
        print("Fizz")
    elif (x % 5) == 0:
        print("Buzz")
    else:
        print (x)
    x = x+1
