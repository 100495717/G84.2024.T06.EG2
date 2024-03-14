import json
from uC3MTravel.hotelManagementException import hotelManagementException
from uC3MTravel.hotelReservation import hotelReservation

class hotelManager:
    def __init__(self):
        pass

    def validatecreditcard( self, x ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        return True

    def readdatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise hotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise hotelManagementException("JSON Decode Error - Wrong JSON "
                                           "Format") from e

        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            req = hotelReservation(iDCARD="12345678Z",creditcardNumb=c,
                                   nAMeAndSURNAME="John Doe",phonenumber=p,roomtype="single",numdays=3)
        except KeyError as e:
            raise hotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise hotelManagementException("Invalid credit card number")

        # Close the file
        return req