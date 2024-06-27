from typing import NewType


class HotDog:
    pass


ReadyToServeHotDog = NewType('ReadyToServeHotDog', HotDog)


def dispense_to_customer(hot_dog: ReadyToServeHotDog):
    print(f"{hot_dog=}")


dispense_to_customer(ReadyToServeHotDog(HotDog()))

