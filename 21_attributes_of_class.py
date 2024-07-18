class Car:
    top_speed = 100
    warnings = []

    def drive(self):
        print(f'I am driving! not faster than {self.top_speed}')


car1 = Car()
car1.drive()
Car.top_speed = 200
print(car1.warnings)
car1.warnings.append('New warning')


car2 = Car()
car2.drive()
print(car2.warnings)

car3 = Car()
car3.drive()
print(car2.warnings)
