#!/usr/bin/env python

import sys
import re

inverse = False

seen = []
for l in sys.stdin.readlines():
    n = l
    seen.append(n)
    assert(n)

    if inverse and n=='\n':
        sys.stdout.write('\n<p class="filler"><br/></p>\n\n')
    else:
        sys.stdout.write(n)

    if n[0]==" ":
        inverse = True
    else:
        inverse = False

    if len(seen)>5:
        seen.pop(0)
