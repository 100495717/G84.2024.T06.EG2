''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib
from HotelManagementException import HotelManagementException
import json

class HotelStay():
    def __init__(self, idcard, localizer, numdays, roomtype):
        self.__alg = "SHA-256"
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)
        self.__room_key = self.room_key

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
    def idCard(self, value):
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
        except FileNotFoundError:
            raise HotelManagementException("No se encuentra el archivo")

        except json.JSONDecodeError:
            raise HotelManagementException("El archivo no tiene formato JSON")
        except Exception as e:
            raise HotelManagementException("Error desconocido")

        localizer = data.get("localizer")
        id_card = data.get("id_card")

        if not localizer or not id_card:
            raise HotelManagementException("El JSON no tiene la estructura correcta")

        with open("reservas.json","r") as f:
            reservas = json.load(f)
        if localizer not in reservas:
            raise HotelManagementException("No hay localizador")

        num_days = data.get("num_days")
        tipo_hab = data.get("room_type")

        instancia = HotelStay(id_card,localizer,num_days,tipo_hab)
        room_key = instancia.room_key

        with open("estancias.json","w") as f:
            json.dump(instancia.__dict__,f)
            f.write('\n')

        return room_key




    def guest_checkout(room_key):
        if not room_key:
            raise HotelManagementException("Introduce una room_key")
        try:
            with open("estancias.json", "r") as f:
                estancias = json.load(f)
        except FileNotFoundError:
            raise HotelManagementException("No se encuentra el archivo de datos")
        except json.JSONDecodeError:
            raise HotelManagementException("El archivo no tiene formato JSON")
        except Exception as e:
            raise HotelManagementException("Error desconocido al procesar el archivo de datos")

        if room_key not in estancias:
            raise HotelManagementException("El código de habitación no está registrado")

        estancia_actual = estancias[room_key]
        departure = estancia_actual["departure"]

        try:
            # Verificar la fecha de salida
            ahora = datetime.utcnow().timestamp()
            if ahora != departure:
                raise HotelManagementException("La fecha de salida no es válida")
            # Registrar la salida en el archivo
            with open("checkout.json", "a") as f:
                checkout_data = {
                    "checkout_time": ahora,
                    "room_key": room_key
                }
                json.dump(checkout_data, f)
                f.write('\n')
            return True
        except Exception as e:
            raise HotelManagementException("Error de procesamiento interno")




