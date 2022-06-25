#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

import sys, re
justblank = False
seen = []
level = 0
nlabels = 0
labels = []

last = 0
for l in sys.stdin.readlines():
    n = l
    seen.append(n)
    assert(n)
    if '<!-- Break -->' in n:
        last += 1
        open('process-%02d.txt'%last, 'w').write(''.join(seen))
        seen = []
