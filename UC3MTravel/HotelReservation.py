
import hashlib
import json
from datetime import datetime

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
        """
        Solicita una reserva de hotel y devuelve un localizador.
        """
        #tengo q poner el json y hacer como que los argumentos que recibe
        # juntarlos en una sola variable para poder hacer
        # datos._validar_datos_reserva
        # Validar datos de entrada
        self._validar_datos_reserva(credit_card_number, id_card,name_surname,
                               phone_number, room_type, arrival, num_days)

        # Crear objeto HotelReservation
        reserva = HotelReservation(id_card, credit_card_number, name_surname,
                                   phone_number, room_type, num_days)

        # Calcular localizador
        localizador = reserva.LOCALIZER

        # Almacenar datos de la reserva en un fichero
        self._almacenar_reserva(reserva)

        return localizador

    def _validar_datos_reserva(self, credit_card_number, id_card, name_surname,
                               phone_number, room_type, arrival, num_days):
        """
        Valida los datos de una reserva.
        """

        # Validar tarjeta de crédito
        if not self._validar_tarjeta_credito(credit_card_number):
            raise ValueError("Número de tarjeta de crédito no válido")

        # Validar DNI
        if not self._validar_dni(id_card):
            raise ValueError("DNI no válido")

        # Validar nombre y apellidos
        if not self._validar_nombre_completo(name_surname):
            raise ValueError("Nombre y apellidos no válidos")

        # Validar número de teléfono
        if not self._validar_telefono(phone_number):
            raise ValueError("Número de teléfono no válido")

        # Validar tipo de habitación
        if room_type not in ("single", "double", "suite"):
            raise ValueError("Tipo de habitación no válido")

        # Validar fecha de llegada
        try:
            datetime.strptime(arrival, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Fecha de llegada no válida")

        # Validar número de días
        if not 1 <= num_days <= 10:
            raise ValueError("Número de días no válido")

    def _validar_tarjeta_credito(self, numero):
        """
        Valida un número de tarjeta de crédito.
        """
        if not isinstance(numero, int) or len(numero) != 16:
            return False

        else:
            luhn = self.luhn(numero)
            if luhn == 0:
                return True
            else:
                return False

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
        return suma % 10

    def _validar_dni(dni):
        """
        Valida un DNI español.
        """
        if len(dni) != 9:
            return False
        else:
            digitos = dni[:-1]
            letra = dni[-1].upper()
            for digito in digitos:
                if digito not in ("0", "1", "2", "3", "4", "5", "6", "7",
                                  "8", "9"):
                    return False
            if letra not in ("A", "B", "C", "D", "E", "F", "G", "H", "I",
                             "J", "K", "L", "M", "N", "O", "P", "Q",
                             "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ):
                return False

            return True





    def _validar_nombre_completo(nombre):
        """
        Valida un nombre completo.
        """
        if len(nombre) < 10 or len(nombre) > 50:
            return False
        else:
            nombre_espacios = nombre.count(" ")
            if nombre_espacios < 1 :
                return False
            else:
                return True


    def _validar_telefono(telefono):
        """
        Valida un número de teléfono.
        """
        if len(telefono) != 9:
            return False
        else:
            for digito in telefono:
                if digito not in ("0", "1", "2", "3", "4", "5", "6", "7",
                                  "8", "9"):
                    return False
            return True


    def _almacenar_reserva(reserva):
        """
        Almacena los datos de una reserva en un fichero.
        """

        # TODO: Implementar el almacenamiento de la reserva

        # Ejemplo: Almacenamiento en CSV

        with open("reservas.csv", "a") as fichero:
            escritor = csv.writer(fichero)
            escritor.writerow([
                reserva.IDCARD,
                reserva.CREDITCARD,
                reserva.NAME_SURNAME,
                reserva.phonenumber,
                reserva.roomtype,
                reserva.ARRIVAL,
                reserva.num_days,
            ])

