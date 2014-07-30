def getter(attr, default=None):
    if isinstance(attr, int) or isinstance(attr, slice):
        def at(obj):
            try:
                return obj[attr]
            except IndexError:
                if default:
                    return default
                raise
        return at
    return lambda obj: getattr(obj, attr, default)