engine = 0

while True:

    command = input('> ').upper()
    if command == 'HELP':
        print(
            '''
start - to start the car
stop - to stop the car
quit - to exit
            ''')
    elif command == 'START':
        if engine == 0:
            print('Car started...Ready to go!')
            engine += 1
        else:
            print('Car has already started')

    elif command == 'STOP':

        if engine == 0:
            print('Car is already stopped')
        else:
            engine = 0
            print('Car stopped')

    elif command == 'QUIT':
        break
    else:
        print("I don't understand that...")
