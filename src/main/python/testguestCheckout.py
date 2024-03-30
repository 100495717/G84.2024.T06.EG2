import unittest
from freezegun import freeze_time
from uc3mTravel.hotelManager import hotelManager
from uc3mTravel.hotelmanagementException import hotelmanagementException



class testGuestcheckout(unittest.TestCase):
    @freeze_time("2024-03-22 00:00:00")
    def testvalidcasecheckout1(self):
        #Ejecuta correctamente
        valor = hotelManager()
        checkout = valor.guestCheckout(
            "52de6a8bb4b91fef1e8c66445ad41d822f9ebc5701af767c719a1af3a052fa68")
        print("Check_out realizado correctamente")
        self.assertEqual(checkout,True)

    def testinvalidcheckout1(self):
        #No introduce room_key
        with self.assertRaises(hotelmanagementException) as cm:
            valor = hotelManager()
            checkout = valor.guestCheckout("")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,
                         "Introduce una room_key")

    def testinvalidcasecheckout2(self):
        #Room_key no registrada
        with self.assertRaises(hotelmanagementException) as cm:
            valor = hotelManager()
            checkout = valor.guestCheckout("9a1b4e7c3d6f2a8b1d5a2b9e1f3d7c4f6a8b2d4e5f9a1b3d6e8f2a4c7d9e3f5")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message,
                         "El código de habitación no está registrado")
