from pydantic import BaseModel
from pydantic.types import DelimitedList


def test_delimited_list():
    SemicolonDelimitedIntList = DelimitedList[';', int]
    class M(BaseModel):
        x: SemicolonDelimitedIntList

    m = M(x='1;2;3', y=['a','b','c'])
    assert m.x == [1, 2, 3]

def test_delimited_list_inline_def():
    class M(BaseModel):
        x: DelimitedList[' ', str]

    m = M(x='words and phrases', y=5)
    assert m.x == ['words', 'and', 'phrases']
