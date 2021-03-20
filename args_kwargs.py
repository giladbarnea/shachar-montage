import click
# from math import sqrt
#
# def safe_sqrt(*args, **kwargs):
#     """Doesn't ever throw an error. Promise."""
#
#     return_value = sqrt(*args, **kwargs)
#     return return_value
from typing import ForwardRef

import pandas as pd

df1 = pd.DataFrame.from_dict()
df2 = pd.DataFrame()

def everwhat(bar):
    return whatever(bar)

def whatever(foo: Foo):
    return Foo


class Foo:
    def __init__(self, bar):
        self.bar = bar
    
    @staticmethod
    def from_emo(foodict) -> Foo:
        return Foo
        
    def to_dict(self) -> dict:
        return {}
    
    def _bla(self, type_):
        pass


foo1 = Foo('baz')
Foo.from_emo({})
foo._bla()
