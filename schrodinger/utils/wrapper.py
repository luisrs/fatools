from schrodinger.structure import Structure


class _StructureWrapper(object):
    def __init__(self, st, index=0):
        assert isinstance(st, Structure), 'st is not a Structure object'
        self.st = st
        self.index = index

    def __getattr__(self, item):
        try:
            try:
                return self.__getprop__(item)
            except AttributeError:
                return getattr(self.st, item)
        except AttributeError:
            raise AttributeError("'{}' object has no attribute '{}'"
                                 .format(self.__class__.__name__, item))

    def __getprop__(self, item):
        try:
            return self.st.property[self.__class__.__prop_key_cache[item]]
        except AttributeError:
            self.__class__.__prop_key_cache = {}
            return self.__getprop__(item)
        except KeyError:
            for key in self.st.property.keys():
                if '_' + item in key:
                    self.__prop_key_cache[item] = key
                    return self.st.property[key]
            raise AttributeError("'{}' object has no attribute '{}'"
                                 .format(self.__class__.__name__, item))

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.st.title)