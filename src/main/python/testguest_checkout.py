from uc3mTravel.hotelManager import hotelManager
import unittest
from freezegun import freeze_time
from uc3mTravel.hotelmanagementException import hotelmanagementException



class testGuestcheckout(unittest.TestCase):
    @freeze_time("2024-03-22 00:00:00")
    def test_valid_case_checkout1(self):
        #Ejecuta correctamente
        valor = hotelManager()
        checkout = valor.guestCheckout(
            "25e7966d648733f9721a9fa9d9e0618e014e516b62e9c48fd2a3fe2e559f3139")
        print("Check_out realizado correctamente")
        self.assertEqual(checkout,True)

    def test_invalid_checkout1(self):
        #No introduce room_key
        with self.assertRaises(hotelmanagementException) as cm:
            valor = hotelManager()
            checkout = valor.guestCheckout("")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,
                         "Introduce una room_key")

    def test_invalid_case_checkout2(self):
        #Room_key no registrada
        with self.assertRaises(hotelmanagementException) as cm:
            valor = hotelManager()
            checkout = valor.guestCheckout("9a1b4e7c3d6f2a8b1d5a2b9e1f3d7c4f6a8b2d4e5f9a1b3d6e8f2a4c7d9e3f5")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,
                         "El código de habitación no está registrado")
