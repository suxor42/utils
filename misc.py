# -*- coding: utf-8 *-*


def coalesce(value, replacement):
    returnvalue = {
        True: value,
        False: replacement
    }
    return returnvalue[value is not None]
