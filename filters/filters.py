import json

class FilterModule(object):
    def filters(self):
        return {
            'getattrsa': getattrsa
        }

def getattrsa(data, attrs):
    results = []

    for entry in data:
        if len(attrs) == 1:
            attr = attrs[0]
            if attr in entry:
                results.append(entry[attr])
        else:
            result = {}
            missing = False

            for attr in attrs:
                if attr in entry:
                    result[attr] = entry[attr]
                else:
                    missing = True

            if missing == False:
                results.append(result)

    return results
