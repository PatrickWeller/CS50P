from seasons import convert_to_minutes, insert_commas
from datetime import timedelta


def test_convert_to_minutes():
    assert convert_to_minutes(timedelta(days=1)) == 1440

def test_insert_commas():
    assert insert_commas(["jim", "pam"]) == "jim, pam"
