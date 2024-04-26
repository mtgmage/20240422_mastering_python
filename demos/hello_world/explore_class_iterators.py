class Product:
    def __init__(self, id: int, name: str, price: float) -> None:
        self.__id = id
        self.__name = name
        self.__price = price

    def __str__(self) -> str:
        return f"{self.__id} {self.__name} {self.__price}"

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price


class CartIterator:
    def __init__(self, items: list) -> None:
        self.__items: list = items
        self.__current_index = -1

    def __next__(self) -> Product:
        self.__current_index += 1
        if self.__current_index >= len(self.__items):
            raise StopIteration()
        return self.__items[self.__current_index]


class Cart:
    def __init__(self) -> None:
        self.__items: list = []

    def add_item(self, product: Product) -> None:
        self.__items.append(product)

    def __iter__(self) -> CartIterator:
        return CartIterator(self.__items)


cart = Cart()
cart.add_item(Product(1, "Apples", 2.34))
cart.add_item(Product(2, "Oranges", 3.25))
cart.add_item(Product(3, "Plums", 4.10))

for la_item in cart:
    print(la_item.name)
