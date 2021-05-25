from input_meta.db_param import param_string
import json
# print(param_string)

param_string = param_string.replace('params:', '')

param_string = param_string.replace('\"', '"')
db_param = json.loads(param_string)

result = []

for param in db_param:
    if isinstance(param, list):
        result.append(param)
    elif isinstance(param, dict):
        pass
    else:
        print('error')
        exit()
        
    print(param)
    print('\n\n')