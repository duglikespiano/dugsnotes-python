class Car:
    # top_speed = 100
    # warnings = []

    def __init__(self, starting_top_speed):
        self.top_speed = starting_top_speed
        self.warnings = []

    def __repr__(self):
        print('printing..')
        return f'top Speed: {self.top_speed}'

    def drive(self):
        print(f'I am driving! not faster than {self.top_speed}')


car1 = Car(100)
car1.drive()
car1.warnings.append('New warning')
print(car1.__dict__)


car2 = Car(200)
car2.drive()


car3 = Car(300)
car3.drive()
