from typing import TypedDict


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float


class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation


def get_nutrition_from_spoonacular(recipe_name: str) -> RecipeNutritionInformation:
    return RecipeNutritionInformation(
        recipes_used=2,
        calories=NutritionInformation(
            value=10,
            unit='kcal',
            confidenceRange95Percent=Range(min=0, max=1),
            standardDeviation=0.5
        ),
        fat=NutritionInformation(
            value=10,
            unit='g',
            confidenceRange95Percent=Range(min=0, max=1),
            standardDeviation=0.5
        ),
        protein=NutritionInformation(
            value=10,
            unit='g',
            confidenceRange95Percent=Range(min=0, max=1),
            standardDeviation=0.5
        ),
        carbs=NutritionInformation(
            value=10,
            unit='g',
            confidenceRange95Percent=Range(min=0, max=1),
            standardDeviation=0.5
        )
    )


nutrition_information: RecipeNutritionInformation = get_nutrition_from_spoonacular("test")
print(f"{nutrition_information=}")
print(f"{nutrition_information.values()=}")

