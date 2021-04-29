from enum import Enum


class Price(Enum):
    MIN = 1500
    AVERAGE = 2300
    MAX = 3100


class CommunicationType(Enum):
    Telephony = 0
    Ir_telephony = 1
    Chat = 2


class CommunicationEquipment:

    def __init__(self, name: str = " ", year_of_production: int = 0,
                 producer: str = " ", price: Price = None, communication_type: CommunicationType = None):
        self.name = name
        self.year_of_production = year_of_production
        self.producer = producer
        self.price = price
        self.communication_type = communication_type

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Year of Production: {self.year_of_production}\n" \
               f"Producer: {self.producer}\n" \
               f"Price: {self.price}\n" \
               f"Communication Type: {self.communication_type}\n"
