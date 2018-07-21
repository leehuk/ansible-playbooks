## append
##   Provides a helper function to append to a list

class FilterModule(object):
    def filters(self):
        filter_list = {
            'append': append
        }

        return filter_list

def append(data, value):
    """Append value to list

    :param data:  Data to append to, in list form
    :param value: Value to append
    :returns:     List
    """
    data.append(value)
    return data
