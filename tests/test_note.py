import pytest

from src.note import rate_note

@pytest.mark.parametrize('note , expected ',[(7, 'unsuccessful'),(8, 'unsuccessful'),(9, 'unsuccessful'), (10,'acceptable'),(11, 'acceptable'),(12,'well'),(13,'well'),(14,'very well'),(15,'very well'),(16,'excellent'),(17,'excellent'),(18,'excellent'),(19,'excellent'),(20,'excellent')])
def test_rate_note_returns_expected_rating(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected




