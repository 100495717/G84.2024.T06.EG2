import unittest
from freezegun import freeze_time
from uc3mTravel.hotelManager import hotelManager
from uc3mTravel.hotelmanagementException import hotelmanagementException
class testHotel(unittest.TestCase):
    @freeze_time("2024-03-26")
    def test_roomReservationvalid(self):
        myReservation = hotelManager()
        value = myReservation.roomReservation(
            credit_card_number="5105105105105100", name_surname="JOSE LOPEZ",
            id_card="12345678N", phone_number="912345678", room_type=
            "single", arrival="21/03/2024", num_days="1")
        self.assertEqual(value, "046a9eb94277ea43bc85659db085cef4")

    def test_roomReservation_novalid1(self):
        #Tarjeta de crédito no valida(no cumple el algoritmo de luhn)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5454545454545458", name_surname="AMADOR "
                                                                    "RIVAS",
                id_card="12346678Z", phone_number="673234897",
                room_type="suite", arrival="28/5/2024", num_days="2")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Número de tarjeta de crédito no válido")


    def main(self):
        unittest.main()

    if __name__ == "main":
        main()



