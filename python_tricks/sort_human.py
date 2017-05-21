import re

def sort_human(l):
    """
    sort a list with indices and letters the way a human would
    :param l: a list of string
    """
    convert = lambda text: float(text) if text.isdigit() else text
    alphanum = lambda key: [ convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key) ]
    l.sort(key=alphanum)
    return l
