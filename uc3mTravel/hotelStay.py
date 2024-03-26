''' Class HotelStay (GE2.2) '''
import json
from datetime import datetime
import hashlib
from uc3mTravel.hotelmanagementException import hotelmanagementException


class hotelStay():
    def __init__(self, idcard, localizer, numdays, roomtype):
        self.__alg = "SHA-256" # pylint: disable=attribute-defined-outside-init
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = str(justnow)
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        self.__departure = str(self.__arrival) + (numdays * 24 * 60 * 60)

    def signatureString(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
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

    @arrival.setter
    def arrival(self, value):
        self.__arrival = value

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

    @property
    def type(self):
        """Returns the issued at value"""
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value











