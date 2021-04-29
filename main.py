from communication_equipment.communication_equipment import Price, CommunicationType
from communication_equipment.phone import Phone
from communication_equipment.comutator import Comutator
from communication_equipment.computer import Computer
from equipment_manager.equipment_manager import EquipmentManager


def main():
    manager = EquipmentManager([
        Phone("Phone", 2019, "Samsung", 2500, "Telephony", 17),
        Comutator("Comutator", 2020, "Atis", 2300, "IR-telephony", 250),
        Computer("Computer", 2017, "Apple", 3100, "Chat", 96)
    ])
    print("_________________________________________________")
    print("Sort producer by alphabet")
    print("_________________________________________________")
    print("\n".join([str(x) for x in manager.sort_by_producer()]))
    print("_________________________________________________")
    print("Search by price")
    print("_________________________________________________")
    print("\n".join([str(x) for x in manager.search_by_price(3100)]))


if __name__ == '__main__':
    main()
