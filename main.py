#THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from uC3MTravel import hotelManager


def main():
    mng = hotelManager()
    res = mng.readdatafromJSOn("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.creditCard)
    print(res.localizer)

if __name__ == "__main__":
    main()
