import json

from doing import Doingdo
from recorder import RecorderFunc, RecorderClass, RecordMode
import recorder as rec
from get_config import get_config

__CONFIG_PATH__ = 'config.local.json'

config = get_config(__CONFIG_PATH__)


@RecorderFunc
def something(ret):
    print(f'somesome {ret}')
    return ret


def func2():
        wow = something(['aaa', 4, 'Morag'])
        print("******************")
        print(wow)

def test_set_record_mode():
    rec.set_mode(RecordMode.RECORD)
    mode = rec.get_mode()
    assert mode == RecordMode.NONE


class Run:

    def func(self):
        a = Doingdo()
        wow = a.somesome(['5', '3', 'shahar'])
        print("******************")
        print(wow)


if __name__=="__main__":

    rec.set_mode(config.is_record)
    Run().func()

    # rec.__is_record__ = config.is_record
    # func2()

