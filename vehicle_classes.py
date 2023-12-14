class Vehicle:
    def __init__(self):
        pass

    def get_type(self):
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__()

    def get_type(self):
        pass


class SmallCar(Car):
    def __init__(self):
        super().__init__()
        self._vehicle_type = 1

    def get_type(self) -> int:
        return self._vehicle_type


class MediumCar(Car):
    def __init__(self):
        super().__init__()
        self._vehicle_type = 2

    def get_type(self) -> int:
        return self._vehicle_type


class BigCar(Car):
    def __init__(self):
        super().__init__()
        self._vehicle_type = 3

    def get_type(self) -> int:
        return self._vehicle_type


class Motorcycle(Vehicle):
    def __init__(self):
        super().__init__()
        self._vehicle_type = 1

    def get_type(self):
        return self._vehicle_type


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self._vehicle_type = 3

    def get_type(self) -> int:
        return self._vehicle_type
