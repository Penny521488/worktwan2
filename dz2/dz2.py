class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
#Додав ввід інформації про власну марку машини
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"
def create_car():
    make = input("Введіть марку автомобіля: ")
    model = input("Введіть модель автомобіля: ")
    year = input("Введіть рік випуску автомобіля: ")
    car = Car(make, model, year)
    return car
user_car = create_car()
print("Інформація про автомобіль:", user_car.get_info())
