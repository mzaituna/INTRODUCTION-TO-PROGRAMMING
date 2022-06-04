import json
class Car:
    carCount = 0
    carId = 0

    # class car def __init__(self):
    def __init__(self):
        dictionary = {}
        self.name = input('Enter car name:')
        self.model = input('What is the model:')
        self.year = input('Year of manufacture:')
        self.price = input('Price of car:')
        Car.carCount += 1
        Car.carId += 1
        print(dictionary)

    # displayCar method of class Car
    def displayCar(self):
        print("Name:", self.name, "Model :", self.model, "ID :", self.carId)

    def dataSave(self):
        dictionary = {"Name:": self.name, "Model :": self.model, "ID :": self.carId,"Year :":self.year, "Price : ": self.price}
        print(dictionary)
        with open('cardata.json', 'w') as convert_file:
            convert_file.write(json.dumps(dictionary))