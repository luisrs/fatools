from schrodinger.structure import StructureReader
from schrodinger.utils import fileutils
from ...utils import wrapper


class Receptor(wrapper._StructureWrapper):
    pass


class Pose(wrapper._StructureWrapper):
    def __eq__(self, other):
        return all(getattr(self, attr) == getattr(other, attr)
                   for attr in ('title', 'lignum', 'posenum'))

    def __repr__(self):
        return '{}({}:{})'.format(self.__class__.__name__,
                                  self.title,
                                  self.posenum)


class PoseViewerFileInvalidError(Exception):
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return 'Pose viewer file is invalid: ' + str(self.filename)


class PoseViewer(object):
    def __init__(self, pvfile):
        self.receptor, self.poses = self.__class__.read_pv_file(pvfile)
        self.filename = pvfile

    @staticmethod
    def read_pv_file(pvfile):
        if not fileutils.is_poseviewer_file(pvfile):
            raise PoseViewerFileInvalidError(pvfile)
        reader = StructureReader(pvfile)
        return (Receptor(reader.next()),
                tuple(Pose(st, i) for i, st in enumerate(reader)))
