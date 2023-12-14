import unittest

from parking_system import ParkingSystem
from vehicle_classes import SmallCar, MediumCar, BigCar, Truck


class TestParkingSystem(unittest.TestCase):
    def test_design_parking_system(self):
        parking_system = ParkingSystem()
        self.assertIsInstance(
            parking_system, ParkingSystem, 'The `parking_system` object was not created successfully.')
        # *** Note: I couldn't decide which of these is better ***
        # if parking_system.__class__ == ParkingSystem:
        if type(parking_system) == ParkingSystem:
            print('The `parking_system` object is created successfully.')

    def test_has_available_slots_attr(self):
        parking_system = ParkingSystem()
        has_available_slots_attribute = hasattr(
            parking_system, "_available_slots")

        self.assertTrue(has_available_slots_attribute,
                        'The _available_slots attribute is not private.')

    def test_incorporate_polymorphism(self):
        small_car = SmallCar()
        medium_car = MediumCar()
        big_car = BigCar()

        small_car_type = small_car.get_type()
        medium_car_type = medium_car.get_type()
        big_car_type = big_car.get_type()

        self.assertEqual(small_car_type, 1)
        self.assertEqual(medium_car_type, 2)
        self.assertEqual(big_car_type, 3)

    def test_parking_system(self):
        parking_system = ParkingSystem([1, 0, 1])
        car1 = SmallCar()
        car2 = SmallCar()
        truck1 = Truck()

        result1 = parking_system.park_vehicle(car1.get_type())
        result2 = parking_system.park_vehicle(truck1.get_type())
        result3 = parking_system.park_vehicle(car2.get_type())

        self.assertTrue(result1)
        self.assertTrue(result2)
        self.assertFalse(result3)


if __name__ == '__main__':
    unittest.main()
