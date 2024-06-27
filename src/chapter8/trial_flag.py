from enum import auto, Flag


class Allergen(Flag):
    FISH = auto()
    SHELLFISH = auto()
    TREE_NUTS = auto()
    PEANUTS = auto()
    GLUTEN = auto()
    SOY = auto()
    DAIRY = auto()


print(f"{Allergen.TREE_NUTS=}")

allergens = Allergen.FISH | Allergen.SHELLFISH
print(f"{allergens=}")

SEAFOOD = Allergen.FISH | Allergen.SHELLFISH
print(f"{SEAFOOD=}")
ALL_NUTS = Allergen.TREE_NUTS | Allergen.PEANUTS
print(f"{ALL_NUTS=}")
