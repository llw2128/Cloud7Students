from CB_IPO import scrape
import pytest as pt
from pytest import mark

@mark.parametrize(
    "input,output",
    [
        (5, "https://www.sec.gov/edgar/search/#/filter_forms=S-1&page=5"),
        (4, "https://www.sec.gov/edgar/search/#/filter_forms=S-1&page=4"),
    ],
)
def test_page_set_mult(input, output):
    tester.reset_url()
    tester.set_page(input)
    assert tester.set_page(input) == output

