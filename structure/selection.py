from abc import ABCMeta, abstractmethod


class Selection(object):
    __metaclass__ = ABCMeta

    def apply(self, st):
        return sorted(self._execute(getattr(st, 'st', st)))

    @abstractmethod
    def _execute(self, st):
        return NotImplemented