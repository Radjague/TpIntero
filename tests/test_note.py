import pytest

from src.note import rate_note

@pytest.mark.parametrize('note , expected ',[(7, 'unsuccessful'),(8, 'unsuccessful'),(9, 'unsuccessful'), (10,'acceptable'),(11, 'acceptable'),(12,'well'),(13,'well')])
def test_rate_note_returns_expected_rating(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected

def test_rate_14_returns_very_well():
    assert rate_note(14) == "very well"
def test_rate_16_returns_excellent():
    assert rate_note(16) == "excellent"
def test_rate_15_returns_very_well():
    assert rate_note(15) == "very well"


