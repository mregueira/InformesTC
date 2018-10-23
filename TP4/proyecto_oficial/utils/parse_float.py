# coding=utf-8
import re


def getText(text):
    regnumber = re.compile(r'^\d+(?:.\d*)?$')

    if not regnumber.match(text.get("1.0", 'end-1c')):
        return None
    else:
        return float(text.get("1.0", 'end-1c'))
