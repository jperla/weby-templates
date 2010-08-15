from __future__ import absolute_import
import types

from . import lib

#TODO: jperla: add tests

#TODO: jperla: add all django filters

class UnicodeException(Exception):
    def __init__(self, item):
        Exception.__init__(self, u'Always work with unicode within your app: %s' % item)

def recursively_iterate(item):
    if isinstance(item, unicode):
        yield item
    elif isinstance(item, str):
        raise UnicodeException(item)
    else:
        for subitem in item:
            for i in recursively_iterate(subitem):
                yield i

def template(join=True):
    def decorator(f):
        def wrapper(*args, **kwargs):
            accumulator = Accumulator()
            f(accumulator, *args, **kwargs)
            if join:
                return ''.join(recursively_iterate(accumulator.accumulated))
            else:
                return accumulator.accumulated
        return wrapper
    return decorator


class Accumulator(object):
    def __init__(self):
        self.stack = []
        self.accumulated = []

    def __catch(self, r):
        if isinstance(r, unicode):
            self.accumulated.append(r)
        elif isinstance(r, str):
            raise UnicodeException(r)
        elif hasattr(r, '__iter__'):
            self.accumulated.append(r) # Assume this is an array (sub-template), just append
        else:
            raise Exception('Unknown object type: %s' % r)

    def __call__(self, r):
        """Accumulates the string.
        Only accepts unicode strings or iterables of strings.
        Adds a newline.
        """
        if isinstance(r, tuple):
            if len(r) == 2:
                start, end = r
                if isinstance(start, str):
                    raise UnicodeException(start)
                if isinstance(end, str):
                    raise UnicodeException(end)
                assert(isinstance(start, unicode))
                assert(isinstance(end, unicode))
                self.__catch(start)
                self.__catch(u'\n')
                self.stack.append(end)
                return self
            else:
                raise Exception('Tuple should be 2-tuple for start/end tags: %s' % r)
        else:
            self.__catch(r)
            self.__catch(u'\n')

    def raw(self, r):
        """Same as __call__.  Does not add a newline.
        """
        self.__catch(r)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.__catch(self.stack.pop())
        self.__catch(u'\n')
