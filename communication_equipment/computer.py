from .communication_equipment import CommunicationEquipment, Price, CommunicationType


class Computer(CommunicationEquipment):
    def __init__(self, name: str = " ", year_of_production: int = 0,
                 producer: str = " ", price: Price = None, communication_type: CommunicationType = None,
                 number_of_keys: float = 0):
        super().__init__(name=name, year_of_production=year_of_production, producer=producer, price=price,
                         communication_type=communication_type)
        self.number_of_keys = number_of_keys

    def __str__(self):
        return f"{super().__str__()}" \
               f"Number of Keys: {self.number_of_keys}\n" \
