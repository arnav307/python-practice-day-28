def list_of_number():
    try:
        number=[]
        for user in range(1,5+1):
            user=int(input('Enter a number: '))
            number.append(user)
        average=sum(number)/len(number)
        print(f"The average of given number is {average}")
    except ValueError:
        print("Please enter numeric number")
        
list_of_number()
