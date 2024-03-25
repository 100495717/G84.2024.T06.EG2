
import hashlib
import json
from datetime import datetime
from HotelManagementException import HotelManagementException

class HotelReservation:
    def __init__(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type,numdays):
        self.__crEDITcardnumber = creditcardNumb
        self.__idcard = IDCARD
        justnow = datetime.utcnow()
        self.__ARRIVAL = datetime.timestamp(justnow)
        self.__NAME_SURNAME = nAMeAndSURNAME
        self.__phonenumber = phonenumber
        self.__roomtype = room_type
        self.__num_days = numdays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + json_info.__str__()
    @property
    def CREDITCARD(self):
        return self.__crEDITcardnumber
    @CREDITCARD.setter
    def CREDITCARD(self, value):
        self.__crEDITcardnumber = value

    @property
    def IDCARD(self):
        return self.__idcard
    @IDCARD.setter
    def IDCARD(self, value):
        self.__idcard = value


    @property
    def LOCALIZER( self ):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()

    def solicitar_reserva_hotel(self, credit_card_number, id_card,name_surname,
                                phone_number, room_type, arrival, num_days):

        if not credit_card_number or id_card or name_surname or \
                phone_number or room_type or arrival or num_days:
            raise HotelManagementException("Faltan datos para la reserva")

        luhn = HotelReservation.luhn(credit_card_number)
        if not(len(credit_card_number) == 16 or
                credit_card_number.isdigit() or luhn):
            raise HotelManagementException(
                "Número de tarjeta de crédito no válido")

        if not (len(id_card) == 9 and id_card.isdigit()):
            raise HotelManagementException("DNI no válido")

        if not (10 <= len(name_surname) <= 50 and len(
                name_surname.split()) >= 2):
            raise HotelManagementException("Nombre y apellidos no válidos")

        if not (len(phone_number) == 9 and phone_number.isdigit()):
            raise HotelManagementException("Número de teléfono no válido")

        if room_type not in ['single', 'double', 'suite']:
            raise HotelManagementException("Tipo de habitación no válido")

        try:
            arrival_date = datetime.strptime(arrival, "%d/%m/%Y")
        except ValueError:
            raise HotelManagementException("Fecha de entrada no válida")

        if not (1 <= num_days <= 10):
            raise HotelManagementException("Número de días no válido")

            # Generar una firma MD5 como identificador de reserva

        localizer = hashlib.md5(self.__str__().encode()).hexdigest()

        reservation_data = {
            "credit_card_number": credit_card_number,
            "id_card": id_card,
            "name_surname": name_surname,
            "phone_number": phone_number,
            "room_type": room_type,
            "arrival": arrival_date,
            "num_days": num_days,
            "localizer": localizer
        }
        # Almacenar los datos de la reserva en un archivo JSON
        with open("reservas.json", "w") as f:
            json.dump(reservation_data, f)
            f.write('\n')

        return localizer

    def luhn(numero):
        suma = 0
        digitos = str(numero)
        digitos_invertidos = digitos[::-1]
        for i, digito in enumerate(digitos_invertidos):
            if i % 2 == 0:
                suma += int(digito)
            else:
                digito_doble = int(digito) * 2
                list_dig_doble = str(digito_doble)
                if len(list_dig_doble) > 1:
                    suma += int(list_dig_doble[0])
                    suma += int(list_dig_doble[1])
                else:
                    suma += digito_doble
        return suma % 10 == 0





