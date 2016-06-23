#!/usr/bin/env python

"""
Copyright (c) 2006-2016 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

import re

from lib.core.settings import WAF_ATTACK_VECTORS

__product__ = "SecureIIS Web Server Security (BeyondTrust)"

def detect(get_page):
    retval = False

    for vector in WAF_ATTACK_VECTORS:
        page, _, _ = get_page(get=vector)
        retval = re.search(r"SecureIIS[^<]+Web Server Protection", page or "") is not None
        retval |= "http://www.eeye.com/SecureIIS/" in (page or "")
        retval |= "?subject=SecureIIS Error" in (page or "")
        if retval:
            break

    return retval
