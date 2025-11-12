import pytest

from src.note import rate_note

@pytest.mark.parametrize('note , expected ',[(7, 'unsuccessful'),(8, 'unsuccessful'),(9, 'unsuccessful'), (10,'acceptable'),(11, 'acceptable')])
def test_rate_note_returns_expected_rating(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected

def test_rate_12_returns_well():
    assert rate_note(12) == "well"

