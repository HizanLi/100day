class notEnoughMoney(Exception):

    def __init__(self):
        print("you do not have enough money")

    pass


class highPressure(Exception):
    def __init__(self):
        print("your pressure level is too high")

    pass
