import pytest

from learning_lab.recipe_scaler import scale_ingredient, scale_recipe


def test_scale_ingredient_adjusts_servings():
    assert scale_ingredient(2, original_servings=4, desired_servings=6) == 3


def test_scale_ingredient_rejects_bad_original_servings():
    with pytest.raises(ValueError):
        scale_ingredient(2, original_servings=0, desired_servings=6)


def test_scale_recipe_updates_each_amount():
    assert scale_recipe({"flour": 2, "sugar": 1}, 4, 2) == {"flour": 1, "sugar": 0.5}
