''' Class HotelStay (GE2.2) '''
import json
from datetime import datetime
import hashlib
from hotelmanagementException import hotelmanagementException


class hotelStay():
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

    def signatureString(self):
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
        return hashlib.sha256(self.signatureString().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value


    def guestArrival(input_file):
        try:
            with open(input_file,"r") as f:
                data = json.load(f)
        except FileNotFoundError:
            raise hotelmanagementException("No se encuentra el archivo")

        except json.JSONDecodeError:
            raise hotelmanagementException("El archivo no tiene formato JSON")
        except Exception as e:
            raise hotelmanagementException("Error desconocido")
        localizer = data.get("localizer")
        idCard = data.get("idCard")

        if not localizer or not idCard:
            raise hotelmanagementException("El JSON no tiene la estructura correcta")

        with open("reservas.json","r") as f:
            reservas = json.load(f)
        if localizer not in reservas:
            raise hotelmanagementException("No hay localizador")

        numDays = data.get("num_days")
        tipohab = data.get("room_type")

        instancia = hotelStay(idCard,localizer,numDays,tipohab)
        roomKey = instancia.room_key

        with open("estancias.json","w") as f:
            json.dump(instancia.__dict__,f)
            f.write('\n')

        return roomKey




    def guestCheckout(room_key):
        if not room_key:
            raise hotelmanagementException("Introduce una room_key")
        try:
            with open("estancias.json", "r") as f:
                estancias = json.load(f)
        except FileNotFoundError:
            raise hotelmanagementException("No se encuentra el archivo de datos")
        except json.JSONDecodeError:
            raise hotelmanagementException("El archivo no tiene formato JSON")
        except Exception as e:
            raise hotelmanagementException("Error desconocido al procesar el archivo de datos")

        if room_key not in estancias:
            raise hotelmanagementException("El código de habitación no está registrado")

        estanciaActual = estancias[room_key]
        departure = estanciaActual["departure"]

        try:
            # Verificar la fecha de salida
            ahora = datetime.utcnow().timestamp()
            if ahora != departure:
                raise hotelmanagementException("La fecha de salida no es válida")
            # Registrar la salida en el archivo
            with open("checkout.json", "a") as f:
                checkoutData = {
                    "checkout_time": ahora,
                    "room_key": room_key
                }
                json.dump(checkoutData, f)
                f.write('\n')
            return True
        except Exception as e:
            raise hotelmanagementException("Error de procesamiento interno")




