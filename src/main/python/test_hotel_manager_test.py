import unittest
from UC3MTravel import HotelManager
class TestHotel(unittest.TestCase):
    def test_room_reservation(self):
        my_reservation = HotelManager()
        value = my_reservation.room_reservation
        self.assertEqual(value,


    if __name__ == "__main__"):
        main()

