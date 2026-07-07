"""Recipe scaling practice helpers."""

from __future__ import annotations


def scale_ingredient(amount: float, original_servings: int, desired_servings: int) -> float:
    """Scale an ingredient amount between serving counts."""
    if original_servings <= 0:
        raise ValueError("original_servings must be positive")
    return round(amount * desired_servings / original_servings, 2)


def scale_recipe(ingredients: dict[str, float], original_servings: int, desired_servings: int) -> dict[str, float]:
    """Scale every ingredient in a recipe."""
    return {
        name: scale_ingredient(amount, original_servings, desired_servings)
        for name, amount in ingredients.items()
    }
