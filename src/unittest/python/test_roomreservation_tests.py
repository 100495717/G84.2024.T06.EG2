import unittest
from freezegun import freeze_time
from uc3m_Travel import hotelManager
from uc3m_Travel import hotelmanagementException
class TestHotel(unittest.TestCase):
    @freeze_time("2024-03-26")
    def test_roomreservationvalid(self):
        myReservation = hotelManager()
        value = myReservation.roomReservation(
            credit_card_number="5105105105105100", name_surname="JOSE LOPEZ",
            id_card="12345678N", phone_number="912345678", room_type=
            "single", arrival="21/3/2024", num_days="1")
        print(value)
        self.assertEqual(value, "046a9eb94277ea43bc85659db085cef4")

    def test_roomreservationnovalid1(self):
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

    def test_roomreservationnovalid2(self):
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

    def test_roomreservationnovalid3(self):
        # Tarjeta de crédito no valida(longitud > 16)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="7653484775675733735", name_surname="DOROTEO RIVAS" ,
                id_card="43521123S", phone_number="717456267",
                room_type="single", arrival="31/9/2024", num_days="4")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "Número de tarjeta de crédito no válido")

    def test_roomreservationnovalid4(self):
        # DNI no válido(longitud < 9)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="4556737586899855", name_surname="CHRIS RAMOS" ,
                id_card="6788345", phone_number="913457872",
                room_type="double", arrival="23/8/2024", num_days="1")
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "DNI no válido")

    def test_roomreservationnovalid5(self):
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

    def test_roomreservationnovalid6(self):
        # Nombre no válido (solo una cadena)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="LACUQUI",
                id_card="63214578Z", phone_number="682589636",
                room_type="SINGLE", arrival="2/5/2024", num_days="7")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Nombre y apellidos no válidos")

    def test_roomreservationnovalid7(self):
        # Nombre no válido (está fuera del rango)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="DJ THEO",
                id_card="63214578Z", phone_number="682589636",
                room_type="SINGLE", arrival="2/5/2024", num_days="7")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Nombre y apellidos no válidos")

    def test_roomreservationnovalid8(self):
        # Nombre no válido (FUERA DEL RANGO POR ENCIMA)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100",
                name_surname="VICTORIA RAFAELA BALMASEDA DE UNZETA Y TELLEZ GIRÓN MARQUESA DE FRANCAVILLA Y SACROMONTE",
                id_card="63214578Z", phone_number="682589636",
                room_type="SINGLE", arrival="2/5/2024", num_days="7")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Nombre y apellidos no válidos")

    def test_roomreservationnovalid9(self):
        # Número de teléfono no válido (no son números)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="AGUSTÍN GORDILLO",
                id_card="63214578Z", phone_number="ajalfa",
                room_type="SINGLE", arrival="2/5/2024", num_days="7")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Número de teléfono no válido")

    def test_roomreservationnovalid10(self):
        # Número de teléfono no válido (no son 9 números)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="PERVIS ESTUPIÑÁN",
                id_card="63214578Z", phone_number="68453",
                room_type="SINGLE", arrival="2/5/2024", num_days="7")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Número de teléfono no válido")

    def test_roomreservationnovalid11(self):
        # Tipo de habitación no válido
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="FRANCISCO PASTOR",
                id_card="63214578Z", phone_number="696966855",
                room_type="5485", arrival="2/5/2024", num_days="7")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Tipo de habitación no válido")

    def test_roomreservationnovalid12(self):
        # Número de días no válido (por encima del rango)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="SERGIO ARIAS",
                id_card="63214578Z", phone_number="696966855",
                room_type="DOUBLE", arrival="2/5/2024", num_days="50")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Número de días no válido")

    def test_roomreservationnovalid13(self):
        # Número de días no válido (por debajo del rango)
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="JAVIER MAROTO",
                id_card="63214578Z", phone_number="696966855",
                room_type="DOUBLE", arrival="2/5/2024", num_days="0")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Número de días no válido")


    def test_roomreservationnovalid14(self):
        # Fecha de entrada no válida
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100", name_surname="ANGELINES CHACÓN",
                id_card="34585853S", phone_number="678096573",
                room_type="SUITE", arrival="diecinueve", num_days="8")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Fecha de entrada no válida")

    def test_roomreservationnovalid15(self):
        # día no válido
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100",
                name_surname="MARIANO DELGADO",
                id_card="52652396L", phone_number="696633525",
                room_type="SUITE", arrival="45/05/2025", num_days="1")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Fecha de entrada no válida")


    def test_roomreservationnovalid16(self):
        # día no válido
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100",
                name_surname="PALOMA CUESTA",
                id_card="88774422P", phone_number="666555444",
                room_type="SUITE", arrival="0/06/2024", num_days="1")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Fecha de entrada no válida")

    def test_roomreservationnovalid17(self):
        # día no válido, mes con 30 dias
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100",
                name_surname="NIEVES CUESTA",
                id_card="11554477Q", phone_number="645312978",
                room_type="SUITE", arrival="31/06/2024", num_days="1")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Fecha de entrada no válida")

    def test_roomreservationnovalid18(self):
        # mes no válido
        myReservation = hotelManager()
        with self.assertRaises(hotelmanagementException) as cm:
            value = myReservation.roomReservation(
                credit_card_number="5105105105105100",
                name_surname="MIKEL OYARZABAL",
                id_card="87452654S", phone_number="699888777",
                room_type="SUITE", arrival="31/14/20274", num_days="1")
        print(cm.exception.message
              )
        self.assertEqual(cm.exception.message, "Fecha de entrada no válida")

    if __name__ == "__main__":
        unittest.main()



