from enum import Enum

class Operation(str, Enum):
    PUBLISH = "publish",
    SAVE_TEMP = "save_temp"