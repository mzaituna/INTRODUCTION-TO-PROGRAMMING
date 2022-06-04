
from car import Car
while True:
    try:
        print('Welcome to CarDataBaseManager!')
        print('What would you like to do ?')
        print('1- Add a car')
        print('2- Search for car')
        print('3- Save the database to file')
        print('4- Remouve a car by id')
        print('5- Quit/n')
        answer = int(input("Please enter your answere: "))
        print('Your answer was: {}'.format(answer))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if answer < 0:
        print("Sorry, your response must not be negative.")
        continue

    elif answer == 1:
        car = Car()
        car.displayCar()

    elif answer == 2:
        print('Search for car')

    elif answer == 3:
        print('Save the database to file')
        car = Car()
        car.dataSave()

    elif answer == 4:
        print('Remouve a car by id')
        print('What do you want to do?')
        print('Enter you choice: ')

    elif answer == 5:
        print('Quit')
        break






