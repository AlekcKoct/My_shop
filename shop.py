
class Store:
    def __init__(self, name, address, items):
        """
        Инициализация объектов.
        :name: Название магазина
        :address: Адрес магазина
        :items: Список товаров в магазине
        """

        self.name = name
        self.address = address
        self.items = items

    def info(self):
        """
        Информация о магазине.
        """
        print(f"\n{self.name}")
        self.name = "Продукты"
        print(f"Адрес: {self.address}")
        print("Ассортимент товаров:")
        for item in self.items:
            print(f"- {item}")

    def info_new(self):
        """
        Изменившаяся информация о магазине.
        """
        print("Ассортимент товаров:")
        for item in self.items:
            print(f"- {item}")

    def info1(self):
        """
        Информация о магазине.
        """

        print(f"\n{self.name}")
        self.name = "Хозтовары"
        print(f"Адрес: {self.address}")
        print("Ассортимент товаров:")
        for item in self.items:
            print(f"- {item}")

    def add_item(self, item):
        """
        :item: Товар для добавления
        """
        self.items.append(item)
        print(f"Товар {item} добавлен в ассортимент магазина {self.name}.")

    def remove_item(self, item1):
        """
        :item1: Товар для удаления
        """
        if item1 in self.items:
            self.items.remove(item1)
            print(f"Товар {item1} удален из ассортимента магазина {self.name}.")
        else:
            print(f"Товар {item1} не найден в ассортименте магазина {self.name}.")

store1 = Store("Магазин для детей", "ул. Сиверса, 210", ["Мяч: 30 руб", "Кукла: 120 руб", "Конструктор: 150 руб"])
store1.info()

store2 = Store("Магазин Продукты", "пр. Буденновский, 122", ["Хлеб: 30 руб", "Молоко: 45 руб", "Яблоки"])
store2.info()
store2.add_item("Сыр: 120 руб")
store2.remove_item("Яблоки")
store2.info_new()

store3 = Store("Магазин Хозтовары", "пр. Буденновский, 233", ["Лопата: 130 руб", "Молоток: 200 руб", "Перфоратор: 2300 руб"])
store3.info1()
store3.add_item("Труба: 75 руб")
store3.info_new()

