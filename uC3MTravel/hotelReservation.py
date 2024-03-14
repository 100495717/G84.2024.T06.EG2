
import hashlib
import json
from datetime import datetime

class hotelReservation:
    def __init__(self, iDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber,
                 roomtype,numdays):
        self.creditCardnumber = creditcardNumb
        self.idCard = iDCARD
        justnow = datetime.utcnow()
        self.arrival = datetime.timestamp(justnow)
        self.nameSurname = nAMeAndSURNAME
        self.phoneNumber = phonenumber
        self.roomType = roomtype
        self.numDays = numdays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        jsonInfo = {"id_card": self.idCard,
                     "name_surname": self.nameSurname,
                     "credit_card": self.creditCardnumber,
                     "phone_number:": self.phoneNumber,
                     "arrival_date": self.arrival,
                     "num_days": self.numDays,
                     "room_type": self.roomType,
                     }
        return "HotelReservation:" + jsonInfo.__str__()
    @property
    def creditCard(self):
        return self.creditCardnumber
    @creditCard.setter
    def creditCard(self, value):
        self.creditCardnumber = value

    @property
    def idCard(self):
        return self.idCard
    @idCard.setter
    def idCard(self, value):
        self.idCard = value


    @property
    def localizer( self ):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()