def fizzbuzz(num):
    for number in range(1, num+1):
        if number%3 == 0 and number%5 == 0:
            print("fizzbuzz")
        elif number%5 == 0:
            print("buzz")
        elif number%3 == 0:
            print("fizz")
        else:
            print(number)
            
fizzbuzz(20)
