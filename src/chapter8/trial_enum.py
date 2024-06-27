from enum import auto, Enum


class MotherSauce(Enum):
    BECHAMEL = auto()
    VELOUTE = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLADAISE = auto()


print(f"{list(MotherSauce)=}")

