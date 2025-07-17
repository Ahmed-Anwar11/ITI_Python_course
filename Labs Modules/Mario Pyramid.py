def mario_pyramid(number):
        for i in range(number):
            number-=1
            i+=1
            print(number*" "+i*"*")

number = int(input("Enter a number:"))
mario_pyramid(number)