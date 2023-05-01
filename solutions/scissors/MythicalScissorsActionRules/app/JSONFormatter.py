import logging
import json
from datetime import datetime


class JSONFormatter(logging.Formatter):

    def __init__(self):
        super().__init__()

    def format(self, record):
        obj_to_dump = {}
        obj_to_dump["timestamp"] = str(datetime.fromtimestamp(record.created))
        obj_to_dump["msg"] = record.msg
        obj_to_dump["levelname"] = record.levelname
        obj_to_dump["funcName"] = record.funcName
        obj_to_dump["filename"] = record.filename
        obj_to_dump["module"] = record.module
        obj_to_dump["name"] = record.name
        record.msg = json.dumps(obj_to_dump)
        return super().format(record)