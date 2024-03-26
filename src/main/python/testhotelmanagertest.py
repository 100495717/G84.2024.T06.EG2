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

    def test_roomReservation_novalid2(self):
        # Tarjeta de crédito no valida(longitud < 16)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="492739871653", name_surname="MAURICIO "
                                                                "HIDALGO",
                id_card="06588879T", phone_number="928432112",
                room_type="double", arrival="29/7/2024", num_days="6")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Número de tarjeta de crédito no válido")

    def test_roomReservation_novalid3(self):
        # Tarjeta de crédito no valida(longitud > 16)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="7653484775675733735", name_surname="DOROTEO RIVAS" ,
                id_card="43521123S", phone_number="717456267",
                room_type="single", arrival="31/9/2024", num_days="4")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Número de tarjeta de crédito no válido")

    def test_roomReservation_novalid4(self):
        # DNI no válido(longitud < 9)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="4556737586899855", name_surname="CHRIS RAMOS" ,
                id_card="6788345", phone_number="913457872",
                room_type="double", arrival="23/8/2024", num_days="1")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "DNI no válido")

    def test_roomReservation_novalid5(self):
        # Tarjeta de crédito no valida(longitud > 9)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="4056787586899855",
                name_surname="LAMINE YAMAL",
                id_card="34214567TRJ", phone_number="643217678",
                room_type="SUITE", arrival="17/5/2024", num_days="3")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "DNI no válido")

    def main(self):
        unittest.main()

    if __name__ == "main":
        main()



