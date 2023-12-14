from functools import reduce


class ParkingSystem:

    def __init__(self, slots: list[int] = [0, 0, 0]) -> None:
        '''Initialize a parking system'''
        self.small, self.medium, self.big = slots
        total_slots = reduce(lambda x, y: x + y, slots)
        self._available_slots = {
            'total_slots': total_slots, 'small_slots': self.small, 'medium_slots': self.medium, 'big_slots': self.big}

    def get_available_slots(self) -> dict:
        '''Return number of each slot size and overall available slots'''
        for key, value in self._available_slots.items():
            print(f'{key}: {value}')

        return self._available_slots

    def set_available_slots(self, slots: list[int]) -> None:
        '''Set number of slots for each car size, track overall parking spaces available.'''
        self.small, self.medium, self.big = slots
        total_slots = reduce(lambda x, y: x + y, slots)

        self._available_slots.update(
            {'total_slots': total_slots, 'small_slots': self.small, 'medium_slots': self.medium, 'big_slots': self.big})

    def park_vehicle(self, vehicle_type: int) -> bool:
        '''Return True upon successful parking of a car, otherwise False'''
        match vehicle_type:
            case 1:
                if self._available_slots['small_slots'] == 0:
                    print('There are no more slots for small cars available.')
                    return False
                else:
                    self._available_slots['small_slots'] -= 1
                    self._available_slots['total_slots'] -= 1
                    return True
            case 2:
                if self._available_slots['medium_slots'] == 0:
                    print('There are no more slots for medium cars available.')
                    return False
                else:
                    self._available_slots['medium_slots'] -= 1
                    self._available_slots['total_slots'] -= 1
                    return True
            case 3:
                if self._available_slots['big_slots'] == 0:
                    print('There are no more slots for big cars available.')
                    return False
                else:
                    self._available_slots['big_slots'] -= 1
                    self._available_slots['total_slots'] -= 1
                    return True
