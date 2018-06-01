import sys
from collections import OrderedDict
from nulltype import NullType

__all__ = 'Empty Item itemize itemize_all'.split()

_PY2 = sys.version_info[0] == 2


Empty = NullType('Empty')


def _item(data):
    """
    Private factory function for Item values, especially second and subsequent
    levels beneath the top-level mapping. Here because recursive initializers
    in Python aren't straightforward (and maybe not really even feasible,
    since some recursions would not yield Item results, but lists or other
    data types).
    """
    # a mapping / dict type => return an Item instead
    if hasattr(data, 'items'):
        it = Item()
        for k, v in data.items():
            it[k] = _item(v)
        return it

    # list or tuple => return exactly that type
    if isinstance(data, (list, tuple)):
        return type(data)(_item(x) for x in data)

    # if not dictionary or sequence, data type is "simple" with respect to
    # Item creation - whether int, float, complex, str, bytes, etc
    return data


class Item(OrderedDict):

    "Ordered, attribute-accessible dictionary/mapping class."

    def __init__(self, a_dict=None, **kwargs):
        super(Item, self).__init__()
        if a_dict:
            for k, v in a_dict.items():
                self[k] = _item(v)
        if kwargs:
            self.update(_item(kwargs))

    def __getattr__(self, name):
        try:
            return super(Item, self).__getitem__(name)
        except KeyError:
            return Empty

    def __setattr__(self, name, value):
        """
        Setting attrs becomes equivalent to setting items.
        """
        self[name] = value

    def __delattr__(self, name):
        try:
            del self[name]
        except KeyError:
            # pass on KeyError for same reason __getattr__ returns Empty if not there:
            # to be permissive in case of missing attributes / keys
            pass

    def __getitem__(self, key):
        try:
            return super(Item, self).__getitem__(key)
        except KeyError:
            return Empty

        # NH explicit action where object.__missing__(self, key) would be called

    # depends on OrderedDict for __delitem__, __setitem__


    def __repr__(self):
        clsname = self.__class__.__name__
        kwstr = ', '.join('{0}={1!r}'.format(k, v) for k, v in self.items())
        return '{0}({1})'.format(clsname, kwstr)


    @classmethod
    def from_tuples(cls, data):
        it = cls()
        for tup in data:
            k, v = tup
            it[k] = _item(v)
        return it


def itemize(iterator):
    """
    Given a collection of dict-like records, create and
    return an Item out of each record.
    """
    for item in iterator:
        yield Item(item)


def itemize_all(iterator):
    """
    Given a collection of dict-like records, create and
    return an list of Item objects comprising all the records.
    """
    return list(itemize(iterator))
