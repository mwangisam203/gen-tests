from learning_lab.booleans import can_drive, exclusive_choice, should_wear_coat


def test_can_drive_requires_age_and_license():
    assert can_drive(18, True)
    assert not can_drive(15, True)
    assert not can_drive(18, False)


def test_should_wear_coat_for_cold_or_rain():
    assert should_wear_coat(45, False)
    assert should_wear_coat(72, True)
    assert not should_wear_coat(72, False)


def test_exclusive_choice_accepts_one_side_only():
    assert exclusive_choice(True, False)
    assert exclusive_choice(False, True)
    assert not exclusive_choice(True, True)
