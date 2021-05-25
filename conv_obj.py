import json
import time
import pprint
from input_meta.db_param import obj



def isTimeFormat(input):
    try:
        time.strptime(input, '%Y-%m-%dT%H:%M:%S+0000')
        return True
    except ValueError:
        return False


def conv(param):
    count = 0
    if isinstance(param, str):
        param = json.loads(param)
    if not isinstance(param, dict):
        print('error')
        exit()
    else:
        
        # print(f"ori param: \n{param}")

        for key, value in param.items():
            if isinstance(value, int) or isinstance(value, float):
                print(f"mp{count}.put(\"{key}\",{value})")
            elif isinstance(value, str):
                if isTimeFormat(value):
                    print(f'dts = "{value}";')
                    print(f'd = sdf.parse(dts);')
                    print(f'mp{count}["{key}"] = d;')
                else:
                    print(f'mp{count}["{key}"] = "{value}";')
            elif value == None:
                print(f'mp{count}["{key}"] = null;')

    count+=1


s = """
{"name": "ric", "age": 23}
"""

obj = json.loads(obj)['arrayOfIbilBillTransDTO'][0]
# pprint.pprint(obj)

conv(obj)

        