from .communication_equipment import CommunicationEquipment, Price, CommunicationType


class Comutator(CommunicationEquipment):
    def __init__(self, name: str = " ", year: int = 0,
                 producer: str = " ", price: Price = None, communication_type: CommunicationType = None,
                 mb: float = 0.0):
        super().__init__(name, year, producer, price, communication_type)
        self.mb = mb

    def __str__(self):
        return f"{super().__str__()}" \
               f"mb : {self.mb}\n"

    def show_speed_ability(self, speed: float = 0.0):
        print(self.mb + speed)
