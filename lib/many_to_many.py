class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name
        self._contracts = []

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be of type Author")
        if not isinstance(book, Book):
            raise TypeError("Book must be of type Book")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        author._contracts.append(self)
        book._contracts.append(self)
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return sorted(
            (contract for contract in cls.all if contract.date == date),
            key=lambda c: c.date
        )