

def translate_to_v2(data_v1):
    data_v2 = {}
    data_v2['user'] = data_v1.get('user')
    data_v2['type'] = data_v1.get('type')
    return data_v2
