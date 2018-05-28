# -*- coding: utf-8 -*-

from items import *
from collections import OrderedDict
import sys


def test_empty():
    it = Item()
    assert list(it.keys()) == []
    assert list(it.values()) == []
    assert list(it.items()) == []
    assert isinstance(it, dict)
    assert isinstance(it, OrderedDict)


def test_simple():
    it = Item(a=1, c=22, b=99, r=4.4, d='this')
    assert list(it.keys()) == 'a c b r d'.split()
    assert list(it.values()) == [1, 22, 99, 4.4, 'this']
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
