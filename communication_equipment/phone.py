from .communication_equipment import CommunicationEquipment, Price, CommunicationType


class Phone(CommunicationEquipment):
    def __init__(self, name: str = " ", year_of_production: int = 0,
                 producer: str = " ", price: Price = None, communication_type: CommunicationType = None,
                 touch_screen_size: int = 0):
        super().__init__(name, year_of_production, producer, price, communication_type)
        self.touch_screen_size = touch_screen_size
        self.price = list[Price]

    def __str__(self):
        return f"{super().__str__()}" \
               f"cm : {self.touch_screen_size}\n"

    def fill(self, price: Price = None):
        self.price.append(price)

    def pour_out(self):
        return self.price
