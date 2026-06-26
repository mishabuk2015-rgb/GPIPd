class Car:
    def __init__(self, model, age, owner=None, fuel=0):
        self.model = model
        self.age = age
        self.owner = owner
        self.fuel = fuel

    def __str__(self):
        return (
            f"Модель: {self.model}\n"
            f"Вік: {self.age}\n"
            f"Власник: {self.owner}\n"
            f"Бензин: {self.fuel} л"
        )

    @property
    def state(self):
        if self.age <= 3:
            return "нове авто"
        elif self.age <= 10:
            return "середній стан"
        else:
            return "старе авто"

    @property
    def fuel_status(self):
        if self.fuel >= 30:
            return "Можна їхати далеко"
        else:
            return "Потрібно заправитись"


car1 = Car("Toyota Camry", 2, "Іван", 20)
car2 = Car("BMW X5", 12, "Петро", 50)

# __dict__
print(car1.__dict__)
print(car2.__dict__)

# print()
print("\nАвто 1:")
print(car1)

print("\nАвто 2:")
print(car2)

# зміна бензину
car1.fuel = 35

print("\nПісля заправки:")
print(car1)

# property
print("\nСтан авто:")
print(car1.state)
print(car2.state)

print("\nСтан пального:")
print(car1.fuel_status)
print(car2.fuel_status)

# порівняння бензину
if car1.fuel > car2.fuel:
    print("\nУ Toyota більше бензину")
elif car2.fuel > car1.fuel:
    print("\nУ BMW більше бензину")
else:
    print("\nКількість бензину однакова")