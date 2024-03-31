import json
from datetime import datetime, timedelta
from pathlib import Path
from .hotelmanagementException import hotelmanagementException
from .hotelReservation import hotelReservation
from .hotelStay import hotelStay


class hotelManager:
    def __init__(self):
        pass

    def validatecreditcard(self, x):
        suma = 0
        digitos = str(x)
        digitosInvertidos = digitos[::-1]
        for i, digito in enumerate(digitosInvertidos):
            if i % 2 == 0:
                suma += int(digito)
            else:
                digitoDoble = int(digito) * 2
                listdigDoble = str(digitoDoble)
                if len(listdigDoble) > 1:
                    suma += int(listdigDoble[0])
                    suma += int(listdigDoble[1])
                else:
                    suma += digitoDoble
        return suma % 10 == 0

    def readdatafromJSOn(self, fi):

        try:
            with open(fi, 'r', encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise hotelmanagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise hotelmanagementException("JSON Decode Error - Wrong JSON "
                                           "Format") from e


        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            req = hotelReservation(idcard="12345678Z",creditcardnumb=c,
                                   nameandsurname="John Doe",phonenumber=p,
                                   room_type="single",numdays=3)
        except KeyError as e:
            raise hotelmanagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise hotelmanagementException("Invalid credit card number")

        # Close the file
        return req

    def roomReservation(self, credit_card_number, id_card, name_surname,
                        phone_number, room_type, arrival, num_days):

        if not credit_card_number or not id_card or not name_surname or not \
                phone_number or not room_type or not arrival or not num_days:
            raise hotelmanagementException("Faltan datos para la reserva")

        luhn = self.validatecreditcard(credit_card_number)
        if (len(credit_card_number) != 16 or not
                credit_card_number.isdigit() or not luhn):
            raise hotelmanagementException("Número de tarjeta de crédito no válido")

        if len(id_card) != 9:
            raise hotelmanagementException("DNI no válido")

        if not (10 <= len(name_surname) <= 50 and len(
                name_surname.split()) >= 2):
            raise hotelmanagementException("Nombre y apellidos no válidos")

        if not (len(phone_number) == 9 and phone_number.isdigit()):
            raise hotelmanagementException("Número de teléfono no válido")

        if room_type.lower() not in ['single', 'double', 'suite']:
            raise hotelmanagementException("Tipo de habitación no válido")

        try:
            arrivalDate = datetime.strptime(arrival, "%d/%m/%Y")
            dia = arrivalDate.day
            mes = arrivalDate.month
            if not 1<= dia <= 31:
                raise hotelmanagementException("El dia introducido no es válido")
            if not 1 <= mes <=12:
                raise hotelmanagementException("Mes no válido")
            if mes not in ("01", "03", "05", "07", "08", "10", "12"):
                if not 1<= dia <=30:
                    raise hotelmanagementException("El dia introducido no es válido")

        except ValueError as exc:
            raise hotelmanagementException("Fecha de entrada no válida") \
                from exc

        if not 1 <= int(num_days) <= 10:
            raise hotelmanagementException("Número de días no válido")


        localizer = hotelReservation(credit_card_number, id_card,
                                       name_surname, phone_number,
                                       room_type, num_days).LOCALIZER

        reservationData = {
            "credit_card_number": str(credit_card_number),
            "id_card": str(id_card),
            "name_surname": str(name_surname),
            "phone_number": str(phone_number),
            "room_type": str(room_type),
            "arrival": str(arrivalDate),
            "num_days": str(num_days),
            "localizer": str(localizer)
        }
        # Almacenar los datos de la reserva en un archivo JSON
        with open(str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/reservas.json")), "w", encoding="utf-8") as f:
            json.dump(reservationData, f)
            f.write('\n')

        return localizer

    def guestArrival(self,input_file):
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as exc:
            raise hotelmanagementException("No se encuentra el archivo") \
                from exc

        except json.JSONDecodeError as exc:
            raise hotelmanagementException("El archivo no tiene formato "
                                           "JSON") from exc
        except Exception as exc:
            raise hotelmanagementException("Error desconocido") from exc
        localizer = data.get("Localizer")
        idCard = data.get("IdCard")
        if not localizer or not idCard:
            raise hotelmanagementException("El JSON no tiene la estructura correcta")
        if len(localizer) > 32:
            raise hotelmanagementException("El localizador está duplicado")
        if len(idCard) > 9:
            raise hotelmanagementException("El DNI está duplicado")

        with open(str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/reservas.json")), "r", encoding="utf-8") as f:
            reservas = json.load(f)
        localizador = reservas.get("localizer")
        numDays = reservas.get("num_days")
        tipohab = reservas.get("room_type")
        arrival = reservas.get("arrival")

        if localizer != localizador:
            raise hotelmanagementException("El localizador no coincide con los datos almacenados")
        instancia = hotelStay(idCard, localizer, numDays, tipohab)
        roomKey = instancia.room_key
        diccionario = {
          "idCard": str(idCard),
          "Localizador": str(localizer),
          "numDays": str(numDays),
          "tipo_hab": str(tipohab),
          "arrival": str(arrival),
          "room_key":str(roomKey),
        }
        with open(str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/estancias.json")), "w", encoding="utf-8") as f:
            json.dump(diccionario, f)
            f.write('\n')

        return roomKey


    def guestCheckout(self, room_key):
        if not room_key:
            raise hotelmanagementException("Introduce una room_key")
        try:
            with open(str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/estancias.json")), "r", encoding="utf-8") as f:
                estancias = json.load(f)
                arrival = estancias.get("arrival")
                numdays = estancias.get("numDays")
        except FileNotFoundError as exc:
            raise hotelmanagementException("No se encuentra el archivo de "
                                           "datos") from exc
        except json.JSONDecodeError as exc:
            raise hotelmanagementException("El archivo no tiene formato "
                                           "JSON") from exc
        except Exception as exc:
            raise hotelmanagementException("Error desconocido al procesar el archivo de datos") from exc

        if room_key != estancias["room_key"]:
            raise hotelmanagementException("El código de habitación no está registrado")

        entra = datetime.strptime(arrival, "%Y-%m-%d %H:%M:%S")
        dias = int(numdays)
        departure = entra + timedelta(days=dias)


        try:
            # Verificar la fecha de salida
            ahora = datetime.utcnow()
            ahoraStr = ahora.strftime("%Y-%m-%d %H:%M:%S")
            if ahora != departure:
                raise hotelmanagementException("La fecha de salida no es válida")
            # Registrar la salida en el archivo
            with open(str(Path.home()) + str(
                Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/checkout"
                     ".json")), "w", encoding ="utf-8") as f:
                checkoutData = {
                    "checkout_time": ahoraStr,
                    "room_key": room_key
                }
                json.dump(checkoutData, f)
                f.write('\n')
            return True
        except Exception as exc:
            raise hotelmanagementException("Error de procesamiento interno")\
                from exc


if __name__ == "__main__":
    valor = hotelManager()
    valorcin = valor.guestArrival(str(Path.home()) + str(Path("/PycharmProjects/G84.2024.T06.EG2/src/JsonFiles/RF2_TEST/valid_test.json")))
    print(valorcin)
