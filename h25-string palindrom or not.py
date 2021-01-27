while True:
    print('___Palindrome or Not____\n')
    s=input('Enter a string or num: ')
    if s.isdigit()==1:
        s1=s[::-1]
        print('_____RESULT of Given NUMBER______')
        print(f'Entered string: {s}\nPalindrome str: {s1}')
        if s==s1:
            print('Entered number is palindrome')
        else:
             print('not plndrm')
    if s.isalpha()==1:
        s1=s[::-1]
        print('_____RESULT oF Given STRING______')
        print(f'Entered string: {s}\nPalindrome str: {s1}')
        if s==s1:
            print('Entered string is palindrome')
        else:
             print('not plndrm')
    print('\n****************NEW*****************')
