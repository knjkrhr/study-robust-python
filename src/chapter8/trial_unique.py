from enum import Enum, unique


@unique
class MotherSauce(Enum):
    BECHAMEL = "ベシャメル"
    BACHAMEL = "ベシャメル"
    VELOUTE = "ヴローテ"
    ESPAGNOLE = "エスパニョール"
    TOMATO = "トマト"
    HOLLANDAISE = "オランデーズ"


mother_source = MotherSauce.BECHAMEL.value
print(f"{mother_source=}")
