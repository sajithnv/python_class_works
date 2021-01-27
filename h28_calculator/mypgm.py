while True:
    from h28_calculator import*
    print('\n** CALCULATOR PROGRAMM**')
    print('________________________')
    print("\n1.Additon\n2.Substraction\n3.Division\n4.Multiplication\n5.Power\n6.Exit")
    a=int(input("\nEnter your choice: "))
    if a==1:
        x=int(input('Enter two num for addition: '))
        y=int(input(': '))
        print('Result is: ',addition(x,y))
    elif a==2:
        x=int(input('Enter two num for subtraction: '))
        y=int(input(': '))
        print('Result is: ',substraction(x,y))
    elif a==3:
        x=int(input('Enter two num for division: '))
        y=int(input(': '))
        print('Result is: ',division(x,y))
    elif a==4:
        x=int(input('Enter two num for multiplication: '))
        y=int(input(': '))
        print('Result is: ',multiplication(x,y))
    elif a==5:
        x=int(input('Enter a num for find the power: '))
        print('Result is: ',power2(x))
    elif a==6:
        print('Program completed Successfully')
        break
    else:
        print('choose a correct choise!!!!!!!!')
