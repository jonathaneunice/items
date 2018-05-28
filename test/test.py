# -*- coding: utf-8 -*-

from items import *
from collections import OrderedDict
import sys

_PY2 = sys.version_info < (3, 0)
_PY36 = sys.version_info >= (3, 6)


def test_empty():
    it = Item()
    assert list(it.keys()) == []
    assert list(it.values()) == []
    assert list(it.items()) == []
    assert isinstance(it, dict)
    assert isinstance(it, OrderedDict)


def test_simple():
    it = Item(a=1, c=22, b=99, r=4.4, d='this')
    keys = 'a c b r d'.split()
    values =  [1, 22, 99, 4.4, 'this']
    if _PY36:
        assert list(it.keys()) == keys
    else:
        assert set(it.keys()) = set(keys)
    if _PY36:
        assert list(it.values()) == values
    else:
        assert set(it.values()) == set(values)
    assert isinstance(it, dict)
    assert isinstance(it, OrderedDict)


def test_Empty():
    e = Empty
    assert e.more.f.d is Empty
    assert e[1].method().there[33][0].no.attributes[99].here is Empty


def test_from_tuples():
    it = Item.from_tuples([('name', 'Susie'),
                           ('age', 12),
                           ('hobby', 'science'),
                           ('friends', ['Dell', 'Bill'])])
    assert it.name == 'Susie'
    assert it.age == 12
    assert it.hobby == 'science'
    assert it.friends == ['Dell', 'Bill']
    assert len(it) == 4
