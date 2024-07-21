import warnings


class Car:
    # top_speed = 100
    # warnings = []

    def __init__(self, starting_top_speed):
        self.top_speed = starting_top_speed
        self.__warnings = []

    def __repr__(self):
        print('printing..')
        return f'top Speed: {self.top_speed}, warnings : ${len(self.__warnings)}'

    def add_warning(self, warning_text):
        if len(warning_text) > 0:
            self.__warnings.append(warning_text)

    def get_warnings(self):
        return self.__warnings

    def drive(self):
        print(f'I am driving! not faster than {self.top_speed}')


car1 = Car(100)
car1.drive()
# car1.__warnings.append('New warning')
car1.add_warning('new warning')

print(car1.get_warnings())
