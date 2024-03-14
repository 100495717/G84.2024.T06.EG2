import unittest
from uC3MTravel import hotelManager
class testHotel(unittest.TestCase):
    def testroomreservation(self):
        myreservation = hotelManager()
        value = myreservation.room_reservation
        self.assertEqual(value)


    if __name__ == ("__main__"):
        main()

