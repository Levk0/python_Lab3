from communication_equipment.communication_equipment import CommunicationEquipment, Price


class EquipmentManager:
    def __init__(self, equipments: list[CommunicationEquipment]):
        self.equipments = equipments

    def sort_by_producer(self, reverse: bool = False):
        return sorted(self.equipments, key=lambda e: e.producer, reverse=reverse)

    def search_by_price(self, price: Price = None):
        result = []
        for i in self.equipments:
            if i.price == price:
                result.append(i)
        return result
