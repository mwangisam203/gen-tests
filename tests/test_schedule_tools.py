from datetime import time

from learning_lab.schedule_tools import minutes_since_midnight, overlaps


def test_overlaps_detects_intersecting_time_ranges():
    assert overlaps(time(9), time(10), time(9, 30), time(11))
    assert not overlaps(time(9), time(10), time(10), time(11))


def test_minutes_since_midnight_counts_hours_and_minutes():
    assert minutes_since_midnight(time(2, 30)) == 150
