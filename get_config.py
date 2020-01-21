
import json
from innolab_utils.utils.jsjson import JsJson


def get_config(config_path='./settings/feedback_scan.json'):
    with open(config_path, 'r') as f:
        meta = json.load(f)
    config = JsJson(meta)

    return config
