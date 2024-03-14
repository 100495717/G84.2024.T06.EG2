''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib

class hotelStay():
    def __init__(self, idcard, localizer, numdays, roomtype  ):
        self.alg = "SHA-256"
        self.type = roomtype
        self.idCard = idcard
        self.localizer = localizer
        justnow = datetime.utcnow()
        self.arrival = justnow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        self.departure = self.arrival + (numdays * 24 * 60 * 60)

    def signatureString(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.alg + ",typ:" + self.type + ",localizer:" + \
            self.localizer + ",arrival:" + self.arrival + \
            ",departure:" + self.departure + "}"

    @property
    def idCard(self):
        """Property that represents the product_id of the patient"""
        return self.idCard

    @idCard.setter
    def icCard(self, value):
        self.idCard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.localizer

    @localizer.setter
    def localizer(self, value):
        self.localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.arrival

    @property
    def roomKey(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.signatureString().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.departure

    @departure.setter
    def departure(self, value):
        self.departure = value