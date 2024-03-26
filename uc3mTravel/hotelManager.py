import json
from datetime import datetime
from uc3mTravel.hotelmanagementException import hotelmanagementException
from uc3mTravel.hotelReservation import hotelReservation



class hotelManager:
    def __init__(self):
        pass

    def validatecreditcard(self, x):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

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

        if not credit_card_number or id_card or name_surname or \
                phone_number or room_type or arrival or num_days:
            raise hotelmanagementException("Faltan datos para la reserva")

        luhn = self.luhn(credit_card_number)
        if not(len(credit_card_number) == 16 or
                credit_card_number.isdigit() or luhn):
            raise hotelmanagementException("Número de tarjeta de crédito no válido")

        if not (len(id_card) == 9 and id_card.isdigit()):
            raise hotelmanagementException("DNI no válido")

        if not (10 <= len(name_surname) <= 50 and len(
                name_surname.split()) >= 2):
            raise hotelmanagementException("Nombre y apellidos no válidos")

        if not (len(phone_number) == 9 and phone_number.isdigit()):
            raise hotelmanagementException("Número de teléfono no válido")

        if room_type not in ['single', 'double', 'suite']:
            raise hotelmanagementException("Tipo de habitación no válido")

        try:
            arrivalDate = datetime.strptime(arrival, "%d/%m/%Y")
        except ValueError as exc:
            raise hotelmanagementException("Fecha de entrada no válida") \
                from exc

        if not (1 <= num_days <= 10):
            raise hotelmanagementException("Número de días no válido")

            # Generar una firma MD5 como identificador de reserva

        localizer = hotelReservation.LOCALIZER

        reservationData = {
            "credit_card_number": credit_card_number,
            "id_card": id_card,
            "name_surname": name_surname,
            "phone_number": phone_number,
            "room_type": room_type,
            "arrival": arrivalDate,
            "num_days": num_days,
            "localizer": localizer
        }
        # Almacenar los datos de la reserva en un archivo JSON
        with open("reservas.json", "w", encoding= "utf-8") as f:
            json.dump(reservationData, f)
            f.write('\n')

        return localizer

    def luhn(self,numero):
        suma = 0
        digitos = str(numero)
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
