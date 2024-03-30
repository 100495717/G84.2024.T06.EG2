from pathlib import Path
import unittest
from freezegun import freeze_time
from uc3mTravel.hotelManager import hotelManager
from uc3mTravel.hotelmanagementException import hotelmanagementException


class testGuestArrival(unittest.TestCase):
    @freeze_time("2024-03-26")
    def testvalidcase(self):
        #Ejecuta correctamente
        rutaArchivo = str(Path.home()) + str(Path(
            "/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/valid_test.json"))
        valor = hotelManager()
        roomKey = valor.guestArrival(rutaArchivo)
        self.assertEqual(roomKey,
                         "52de6a8bb4b91fef1e8c66445ad41d822f9ebc5701af767c719a1af3a052fa68")
    def testdupcorch1(self):
        #Tiene el primer corchete duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_corch1.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testdupcorch2(self):
        #Tiene el segundo corchete duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_corch2.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnocorch1(self):
        #No tiene el primer corchete
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_corch1.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnocorch2(self):
        #No tiene el segundo corchete
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_corch2.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testdupcoma(self):
        #Tiene la coma entre módulos duplicada
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_coma.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnocoma(self):
        #No tiene la coma entre módulos
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_coma.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testno1stmodule(self):
        #No existe el primer módulo
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_1stmodule.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El JSON no tiene la estructura correcta")

    def testno2ndmodule(self):
        #No existe el segundo módulo
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_2ndmodule.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testduplocalizer(self):
        #El localizador está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_Localizer.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnoLocalizer(self):
        #El localizador no existe
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_Localizer.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testdupdosp1(self):
        #Tiene los dos puntos del Localizer duplicados
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_dospuntos1.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnodosp1(self):
        #No tiene los dos puntos del Localizer
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_dospuntos1.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testduplocalizador(self):
        #El valor del localizador está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_localizador.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El localizador está duplicado")
    def testnolocalizador(self):
        #El localizador está vacío
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_localizador.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")
    def testdupIdcard(self):
    #El IDCARD está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_IDCARD.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnoIdcard(self):
        #El IDCARD no existe
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_IDCARD.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testdupdosp2(self):
    #Los dos puntos del IDCARD están duplicados
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_dospuntos2.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testnodosp2(self):
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_dospuntos2.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El archivo no tiene formato JSON")

    def testdupdni(self):
    #El contenido de IDCARD está duplicado
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/dup_dni.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El DNI está duplicado")

    def testnodni(self):
        # El contenido de IDCARD está vacío
        with self.assertRaises(hotelmanagementException) as cm:
            rutaArchivo = str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/no_dni.json"))
            valor = hotelManager()
            roomKey = valor.guestArrival(rutaArchivo)
        print(cm.exception.message)
        self.assertEqual(cm.exception.message, "El JSON no tiene la estructura correcta")



if __name__ == "__main__":
    unittest.main()


