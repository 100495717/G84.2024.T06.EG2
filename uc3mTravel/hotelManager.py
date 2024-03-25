import json
from hotelmanagementException import hotelmanagementException
from hotelReservation import hotelReservation

class hotelManager:
    def __init__(self):
        pass

    def validatecreditcard(self, x):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def readdatafromJSOn(self, fi):

        try:
            with open(fi) as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise hotelmanagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise hotelmanagementException("JSON Decode Error - Wrong JSON "
                                           "Format") from e


        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            req = hotelReservation(IDCARD="12345678Z",creditcardNumb=c,
                                   nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise hotelmanagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise hotelmanagementException("Invalid credit card number")

        # Close the file
        return req