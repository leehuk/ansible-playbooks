import json

class FilterModule(object):
    def filters(self):
        return {'getdest': getdest}

def getdest(data):
    results = []

    for entry in data:
        if 'path' in entry:
            results.append(entry['path'])
        if 'dest' in entry:
            results.append(entry['dest'])

    return results
