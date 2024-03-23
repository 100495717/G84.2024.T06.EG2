''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib
from HotelManagementException import HotelManagementException
import json

class HotelStay():
    def __init__(self, idcard, localizer, numdays, roomtype  ):
        self.__alg = "SHA-256"
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + self.__arrival + \
            ",departure:" + self.__departure + "}"

    @property
    def idCard(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @idCard.setter
    def icCard(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value


    def guest_arrival(input_file):
        try:
            with open(input_file,"r") as f:
                data = json.load(f)
            localizador = data.get("Localizer")
            idcard = data.get("IdCard")

            if not localizador or not idcard:
                raise HotelManagementException("Faltan datos en el JSON")
        except json.JSONDecodeError as e:
            raise HotelManagementException("No tiene formato JSON")
        except KeyError as e:
            raise HotelManagementException("El JSON no tiene la estructura correcta")

            if not isinstance(localizador,str) or not isinstance(idcard,str):
                raise ValueError
        except ValueError:
            raise HotelManagementException("Los datos del JSON no son válidos")
        if localizador != self.__localizer:
            raise HotelManagementException("El localizador no se corresponde con el del archivo")
        try:
            arrival = datetime.strptime(data.get("Arrival"),"%DD-%MM-%AAAA")
        except ValueError:
            raise HotelManagementException("La fecha de llegada no tiene el formato válido")
        if arrival != self.__arrival:
            raise HotelManagementException("La fecha de llegada no se corresponde con la del archivo")

        clave = self.room_key()
        with open("estancias.json","a") as f:
            data = {"localizador": self.__localizer,
                    "idcard": self.__idcard,
                    "arrival": self.__arrival.isoformat(),
                    "departure": self.__departure.isoformat(),
                    "room_key": clave
                    }
            json.dump(data,f)
        return clave

    def room_key(self):
        try:
            return hashlib.sha256(self.__signature_string().encode()).hexdigest()
        except Exception as e:
            raise HotelManagementException("Error de procesamiento interno")



