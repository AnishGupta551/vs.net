import database


filename = input('enter database to connect to: ')
file = open(filename, 'a')
file.close()

while True:
    option = input('enter a to append, f to find, d to delete, u to update, and q to quit: ')
    
    if option == 'a':
        key = input('enter key: ')
        value = input('enter value: ')
        database.insert(filename, key, value)
        print('row appended')

    elif option == 'f':
        key = input('enter key: ')
        print(database.select_one(filename, key))
        
    elif option == 'd':
        key = input('enter key: ')
        database.delete(filename, key)
        
    elif option == 'u':
        key = input('enter key: ')
        value = input('enter value: ')
        database.update(filename, key, value)
    
    elif option == 'q':
        break
        
    else:
        print(option, 'is not a valid input')