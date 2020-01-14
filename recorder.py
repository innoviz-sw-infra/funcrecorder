import pickle
from enum import Enum
from functools import wraps
# https://www.geeksforgeeks.org/class-as-decorator-in-python/
# TODO how to control static variable in python... in class or in module level? how to avoid shadowing (redecleration)


class RecordMode(Enum):
    N0NE = 0
    RECORD = 1
    REPLAY = 2


class RecordMgr:
    __RecordFileName__ = "recorder"
    # __is_record__ = 2

    def __init__(self):
        self.index = 0
        self.__record_mode__ = 0

    @property
    def record_path(self):
        # return f"tmp/recorder/{self.func_name}/{self.__RecordFileName__}_{self.index}.pickle"
        return f"C:\\Development\\prema_line_tester\\{self.__RecordFileName__}_{self.index}.pickle"

    def store(self, val):
        with open(self.record_path, 'wb') as file:
            pickle.dump(val, file)
        self.index += 1

    def replay(self):
        val = None
        with open(self.record_path, 'rb') as file:
            val = pickle.load(file)
        self.index += 1
        return val


recorder = RecordMgr()


def set_mode(mode):
    recorder.__record_mode__ = mode


def get_mode():
    return recorder.__record_mode__


def RecorderClass(f):
    @wraps(f)
    def _impl(self, *args, **kwargs):
        if recorder.__record_mode__ == 0:#RecorderMode.N0NE.value:
            #do nothing
            return f(self, *args, **kwargs)

        elif recorder.__record_mode__ == 1:#RecorderMode.RECORD.value:
            val = f(self, *args, **kwargs)
            # store val
            recorder.store(val)
            return f(self, *args, **kwargs)

        elif recorder.__record_mode__ == 2:#RecorderMode.REPLAY.value:
            # replay val
            val = recorder.replay()
            # print(val)
            return val
    return _impl


class RecorderFunc(object):
    __RecordFileName__ = "recorder"

    def __init__(self, f):
        self.f = f
        self.index = 0


    @property
    def func_name(self):
        return self.f.__name__

    @property
    def record_path(self):
        # return f"tmp/recorder/{self.func_name}/{self.__RecordFileName__}_{self.index}.pickle"
        return f"C:\\Development\\prema_line_tester\\{self.__RecordFileName__}_{self.index}.pickle"

    def store(self, val):
        with open(self.record_path, 'wb') as file:
            pickle.dump(val, file)
        self.index += 1

    def replay(self):
        val = None
        with open(self.record_path, 'rb') as file:
            val = pickle.load(file)
        self.index += 1
        return val

    def __call__(self, *argv, **kwargs):
        if self.__is_record__ == 0:#RecorderMode.N0NE.value
            #do nothing
            return self.f(*argv, **kwargs)

        elif self.__is_record__ == 1:#RecorderMode.RECORD.value:
            val = self.f(*argv, **kwargs)
            # store val
            self.store(val)
            return self.f(*argv, **kwargs)
        elif self.__is_record__ == 2:#RecorderMode.REPLAY.value:
            # replay val
            val = self.replay()
            # print(val)
            return val


