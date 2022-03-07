while True:
    print('''
    Let's find out if you are willing to wait long enough to get the thing you want!
    Only type numbers for each of the following inputs.''')
    
    invest = int(input('How much do you want to invest each month? \n'))
    required = int(input('How much do you need to have? \n'))
    time = int(input('How long are you willing to wait? Enter the amount of months. \n'))
    
    if required/invest<=time:
        print('You will have to save for '+str(int(required/invest))+' months')
    else:
        print('You aren\'t willing to wait long enough. You need greater patience.')
        break