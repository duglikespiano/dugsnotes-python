class Car:
    # top_speed = 100
    # warnings = []

    def __init__(self, starting_top_speed):
        self.top_speed = starting_top_speed
        self.warnings = []

    def drive(self):
        print(f'I am driving! not faster than {self.top_speed}')


car1 = Car(100)
car1.drive()
# Car.top_speed = 200
print(car1.warnings)
car1.warnings.append('New warning')


car2 = Car(200)
car2.drive()
print(car2.warnings)

car3 = Car(300)
car3.drive()
print(car2.warnings)
