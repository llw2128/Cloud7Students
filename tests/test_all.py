from resources import StudentsResource
import pytest as pt
from pytest import mark

tester = StudentsResource()

def test_init():
    assert tester.get_students() is None

