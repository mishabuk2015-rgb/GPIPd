from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, fuel, condition):
        self.fuel = fuel
        self.condition = condition

    @property
    def is_working(self):
        return self.condition > 30

    @abstractmethod
    def __str__(self):
        pass

    def move(self, distance):
        if not self.is_working:
            print("Транспорт несправний!")
            return

        if self.fuel < distance:
            print("Недостатньо пального!")
            return

        self.fuel -= distance
        self.condition -= distance // 2

        if self.condition < 0:
            self.condition = 0

        print(f"Транспорт проїхав {distance} км.")


class Car(Transport):
    def __init__(self, model):
        super().__init__(50, 100)
        self.model = model

    def __str__(self):
        return f"Car: {self.model}, Паливо: {self.fuel}, Стан: {self.condition}"


class Truck(Transport):
    def __init__(self, name):
        super().__init__(120, 100)
        self.name = name

    def __str__(self):
        return f"Truck: {self.name}, Паливо: {self.fuel}, Стан: {self.condition}"


class Motorcycle(Transport):
    def __init__(self, brand):
        super().__init__(20, 100)
        self.brand = brand

    def __str__(self):
        return f"Motorcycle: {self.brand}, Паливо: {self.fuel}, Стан: {self.condition}"


class ServiceStation:
    def repair(self, transport_unit: Transport):
        transport_unit.condition += 30
        if transport_unit.condition > 100:
            transport_unit.condition = 100
        print("Транспорт відремонтовано!")




car = Car("Toyota")
truck = Truck("MAN")
motorcycle = Motorcycle("Honda")

print(car)
print(truck)
print(motorcycle)

print()

car.move(20)
print(car)

print()

print("is_working:", car.is_working)
print(car.__dict__)

print()


motorcycle.move(30)

print()

car.condition = 20
print(car.is_working)
car.move(5)

print()

service = ServiceStation()

truck.condition = 70
service.repair(truck)
print(truck)

print()


car.condition = 0
service.repair(car)
print(car)

print()

service.repair(car)
service.repair(car)
print(car)
#