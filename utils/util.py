# coding=utf-8

__author__ = 'lipf'


class EnumMap(object):

    @staticmethod
    def enum(*sequential, **named):
        enums = dict(zip(sequential, map(str, range(1, (len(sequential)+1)))), **named)
        reverse_enums = dict((value, key) for key, value in enums.iteritems())
        enums['display'] = reverse_enums
        return type('Enum', (), enums)


class StripJsOb(object):
    def __init__(self, **kwds):
        super(StripJsOb, self).__init__()
        for k, v in kwds.iteritems():
            if isinstance(v, basestring):
                if "\n" not in v:
                    _v = v.strip()
                    if _v != v:
                        kwds[k] = _v
        self.__dict__.update(kwds)
