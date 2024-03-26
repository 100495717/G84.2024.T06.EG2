from uc3mTravel.hotelManager import hotelManager
import unittest
from freezegun import freeze_time  # Asumiendo que necesitas esta importación
from pathlib import Path
# Crea un nuevo archivo (por ejemplo, test_hotelManager.py)

class testGuestArrival(unittest.TestCase):
    @freeze_time("2024-03-26")
    def test_valid_case(self):
        ruta_archivo = str(Path.home()) + str(Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/valid_test.json"))
        valor = hotelManager()
        valorcin = valor.guestArrival(ruta_archivo)
        print(valorcin)
        self.assertEqual(valorcin,"52de6a8bb4b91fef1e8c66445ad41d822f9ebc5701af767c719a1af3a052fa68")
if __name__ == "__main__":
    unittest.main()  # Ejecuta las pruebas (ubicadas al final)


