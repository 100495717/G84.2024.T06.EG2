import json
from datetime import datetime
from uc3mTravel.hotelmanagementException import hotelmanagementException
from uc3mTravel.hotelReservation import hotelReservation


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

        if (len(id_card) != 9):
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
            dia = arrivalDate.timetuple().tm_yday
            mes = arrivalDate.month
            if not 1<= dia <= 31:
                raise hotelmanagementException("El dia introducido no es válido")
            if 1 <= mes <=12:
                raise hotelmanagementException("Mes no válido")
            if mes not in ("01", "03", "05", "07", "08", "10", "12"):
                if not 1<= dia <=30:
                    raise hotelmanagementException("El dia introducido no es válido")

        except ValueError as exc:
            raise hotelmanagementException("Fecha de entrada no válida") \
                from exc

        if not (1 <= int(num_days) <= 10):
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
        with open("reservas.json", "w", encoding= "utf-8") as f:
            json.dump(reservationData, f)
            f.write('\n')

        return localizer

