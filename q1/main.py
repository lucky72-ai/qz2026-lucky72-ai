import json
import os
def analyze_log(filepath: str) -> dict:
    result={
        "total":0,
        "by_level":{},
        "by_user":{},
        "last_error":""
    }
if not os.path.exists(filepath)
    return result
with open(filepath,"r",encoding='utf-8') as f
    for line in f:
        if not line:
            continue
        try:
            data=json.loads(line)
        except:
            continue
        result['total']+=1