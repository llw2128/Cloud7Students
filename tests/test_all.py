from resources.students import StudentsResource
import pytest as pt
from pytest import mark

tester = StudentsResource()

@mark.parametrize("output",[({
        "uni": "ffn2000",
        "first_name": "Rona",
        "last_name": "Bernardinelli",
        "email": "ffn2000@columbia.edu",
        "school": "SEAS",
        "year": 4
    })])
def test_init(output):
    assert output in tester.get_students()

