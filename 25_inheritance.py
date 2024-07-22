class Car:
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


class Bus(Car):
    def __init__(self, starting_top_speed):
        super().__init__(starting_top_speed)
        self.passengers = []

    # def __repr__(self):
    #     print('printing..')
    #     return f'top Speed: {self.top_speed}, warnings : ${len(self.__warnings)}'

    # def add_warning(self, warning_text):
    #     if len(warning_text) > 0:
    #         self.__warnings.append(warning_text)

    # def get_warnings(self):
    #     return self.__warnings

    # def drive(self):
    #     print(f'I am driving! not faster than {self.top_speed}')

    def add_group(self, passengers):
        self.passengers.extend(passengers)


bus1 = Bus(100)
bus1.add_group(['dug', 'doremi', 'blahblah'])
bus1.drive()
print(bus1.passengers)
