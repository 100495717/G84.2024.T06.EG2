from datetime import datetime
import hashlib


class hotelReservation:
    def __init__(self, idcard, creditcardnumb, nameandsurname, phonenumber,
                 room_type,numdays):
        justnow = datetime.utcnow()
        self.__ARRIVAL = datetime.timestamp(justnow)
        self.__NAME_SURNAME = nameandsurname
        self.__phonenumber = phonenumber
        self.__roomtype = room_type
        self.__num_days = numdays
        self.__crEDITcardnumber = creditcardnumb
        self.__idcard = idcard

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        jsonInfo = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + jsonInfo.__str__()
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

    @property
    def ARRIVAL(self):
        return self.__ARRIVAL

    @ARRIVAL.setter
    def ARRIVAL(self, value):
        self.__ARRIVAL = value

    @property
    def NAME_SURNAME(self):
        return self.__NAME_SURNAME

    @NAME_SURNAME.setter
    def NAME_SURNAME(self, value):
        self.__NAME_SURNAME = value

    @property
    def PHONENUMBER(self):
        return self.__phonenumber

    @PHONENUMBER.setter
    def PHONENUMBER(self, value):
        self.__phonenumber = value

    @property
    def ROOMTYPE(self):
        return self.__roomtype

    @ROOMTYPE.setter
    def ROOMTYPE(self, value):
        self.__roomtype = value

    @property
    def NUMDAYS(self):
        return self.__num_days

    @NUMDAYS.setter
    def NUMDAYS(self, value):
        self.__num_days = value