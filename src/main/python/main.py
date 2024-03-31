#THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from src.main.python.uc3m_Travel.hotelManager import hotelManager


def main():
    mng = hotelManager()
    res = mng.readdatafromJSOn("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.CREDITCARD)
    print(res.LOCALIZER)

if __name__ == "__main__":
    main()
