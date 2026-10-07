import json
import os
def analyze_log(filepath: str) -> dict:
    result={
        "total":0,
        "by_level":{},
        "by_user":{},
        "last_error":""
    }
