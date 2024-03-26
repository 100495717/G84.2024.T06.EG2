from uc3mTravel.hotelManager import hotelManager
import unittest
from freezegun import freeze_time
from pathlib import Path
from uc3mTravel.hotelmanagementException import hotelmanagementException


class testGuestArrival(unittest.TestCase):
    @freeze_time("2024-03-26")
    def test_valid_case(self):
        #Ejecuta correctamente
        ruta_archivo = str(Path.home()) + str(Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/valid_test.json"))
        valor = hotelManager()
        room_key = valor.guestArrival(ruta_archivo)
        self.assertEqual(room_key,"52de6a8bb4b91fef1e8c66445ad41d822f9ebc5701af767c719a1af3a052fa68")
    def test_dup_corch1(self):
        #Tiene el primer corchete duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_corch1.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_corch2(self):
        #Tiene el segundo corchete duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_corch2.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_corch1(self):
        #No tiene el primer corchete
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_corch1.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_corch2(self):
        #No tiene el segundo corchete
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_corch2.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_coma(self):
        #Tiene la coma entre módulos duplicada
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_coma.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_coma(self):
        #No tiene la coma entre módulos
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_coma.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_1stmodule(self):
        #No existe el primer módulo
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_1stmodule.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El JSON no tiene la estructura correcta")

    def test_no_2ndmodule(self):
        #No existe el segundo módulo
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_2ndmodule.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_localizer(self):
        #El localizador está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_Localizer.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_Localizer(self):
        #El localizador no existe
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_Localizer.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_dosp1(self):
        #Tiene los dos puntos del Localizer duplicados
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_dospuntos1.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_dosp1(self):
        #No tiene los dos puntos del Localizer
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_dospuntos1.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_localizador(self):
        #El valor del localizador está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_localizador.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El localizador está duplicado")
    def test_no_localizador(self):
        #El localizador está vacío
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_localizador.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")
    def test_dup_IDCARD(self):
    #El IDCARD está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_IDCARD.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_IDCARD(self):
        #El IDCARD no existe
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_IDCARD.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_dosp2(self):
    #Los dos puntos del IDCARD están duplicados
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_dospuntos2.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_no_dosp2(self):
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_dospuntos2.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def test_dup_dni(self):
    #El contenido de IDCARD está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_dni.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El DNI está duplicado")

    def test_no_dni(self):
        # El contenido de IDCARD está vacío
        with self.assertRaises(hotelmanagementException) as cm:
            ruta_archivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_dni.json"))
            valor = hotelManager()
            room_key = valor.guestArrival(ruta_archivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El JSON no tiene la estructura correcta")



if __name__ == "__main__":
    unittest.main()


