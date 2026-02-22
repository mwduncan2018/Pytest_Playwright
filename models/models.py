from dataclasses import dataclass

@dataclass
class ProductModel:
    manufacturer: str
    model: str
    price: int
    numberInStock: int

@dataclass
class EntryModel:
    manufacturer: str
    model: str