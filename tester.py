import json

from doing import Doingdo
from recorder import RecorderFunc, RecorderClass, RecordMode
import recorder as rec

__CONFIG_PATH__ = 'config.local.json'


@RecorderFunc
def something(ret):
    print(f'somesome {ret}')
    return ret


def func2():
        wow = something(['5', '3', 'shahar'])
        print("******************")
        print(wow)

def test_set_record_mode():
    rec.set_mode(RecordMode.RECORD)

    mode = rec.get_mode()

    assert mode == RecordMode.RECORD

class Run:

    def func(self):
        a = Doingdo()
        wow = a.somesome(['5', '3', 'shahar'])
        print("******************")
        print(wow)


if __name__=="__main__":
    # Run().func()
    #
    # RecorderFunc.__is_record__ = 2
    #
    test_set_record_mode()
    # func2()
